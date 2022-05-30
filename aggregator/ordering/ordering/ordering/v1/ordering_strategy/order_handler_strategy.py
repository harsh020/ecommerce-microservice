import abc
import logging

from django.conf import settings

from utils.request.request.request_interface import IRequest


class OrderHandlerStrategy(abc.ABC):
    def __init__(self, request_handler: IRequest) -> None:
        self._request = request_handler

    @abc.abstractmethod
    def place_order(self, request, *args, **kwargs):
        raise NotImplemented('Concrete implementation of method not found')

    @abc.abstractmethod
    def cancel_order(self, request, *args, **kwargs):
        raise NotImplemented('Concrete implementation of method not found')


class EagerOrderHandlerStrategy(OrderHandlerStrategy):
    def _create_endpoint(self, service, method):
        base_url = service['url']
        route = service['api'][method.upper()]
        return f'{base_url}{route}'

    def place_order(self, request, *args, **kwargs):
        data = request.data
        logging.info('#'*50)
        logging.info(f'Placing order with data {data}')

        payment_data = data.pop('payment')

        # 1. Create Order
        # print(type(data))
        order = self._request.post(url=self._create_endpoint(settings.ORDER_SERVICE, 'create'),
                                   json=data)
        logging.info(f'Created order {order}')

        # 2.1. Crete payment
        payment_data['order'] = order['id']
        payment_data['order_number'] = order['order_number']
        payment_data['customer'] = order['customer']
        payment = self._request.post(url=self._create_endpoint(settings.PAYMENT_SERVICE, 'create'),
                                     json=payment_data)
        logging.info(f'Created payment {payment}')

        # 2.2 Update order
        update_data = {
            'payment': payment['id']
        }
        update_endpoint = self._create_endpoint(settings.ORDER_SERVICE, 'update')
        update_endpoint = update_endpoint.format(id=order['id'])
        order = self._request.patch(url=update_endpoint, json=update_data)
        order['payment'] = payment
        logging.info(f'Updated order {order}')

        # 3. Update Inventory
        order_items = data.pop('order_items')
        for order_item in order_items:
            order_item = {
                'product': order_item['product'],
                'quantity': order_item['quantity'],
                'price': order_item['price']
            }
            update_endpoint = self._create_endpoint(settings.PRODUCT_SERVICE, 'update')
            update_endpoint = update_endpoint.format(id=order_item['product'])
            updated_data = {
                'count_in_stock': order_item['quantity']
            }
            self._request.patch(url=update_endpoint, data=updated_data)
        logging.info(f'Updated inventory')

        # 4. Clear Cart
        delete_endpoint = self._create_endpoint(settings.CART_SERVICE, 'delete')
        delete_endpoint = delete_endpoint.format(customer=data['customer'])
        self._request.delete(url=delete_endpoint)
        logging.info(f'Cleared cart')
        logging.info('#' * 50)

        # TODO: 5. Store in redis with callback with timout of 20 min to check if
        #          order payment fails then cancel the order.

        return order

    def cancel_order(self, request, *args, **kwargs):
        data = request.data

        # 1. Update order status to Cancelled
        update_data = {
            'status': 'CL'
        }
        update_endpoint = self._create_endpoint(settings.ORDER_SERVICE, 'update')
        update_endpoint = update_endpoint.format(id=data['order'])
        order = self._request.patch(url=update_endpoint, json=update_data)
        logging.info(f'Order cancelled {order}')

        # 2. Update payment status to Refund
        update_data = {
            'status': 'RE'
        }
        update_endpoint = self._create_endpoint(settings.PAYMENT_SERVICE, 'update')
        update_endpoint = update_endpoint.format(id=order['payment'])
        payment = self._request.patch(url=update_endpoint, json=update_data)
        order['payment'] = payment
        logging.info(f'Payment updated {payment}')

        # 3. Update Inventory
        for order_item in order['order_items']:
            order_item = {
                'product': order_item['product'],
                'quantity': order_item['quantity'],
                'price': order_item['price']
            }
            update_endpoint = self._create_endpoint(settings.PRODUCT_SERVICE, 'update')
            update_endpoint = update_endpoint.format(id=order_item['product'])
            updated_data = {
                'count_in_stock': order_item['quantity']
            }
            self._request.patch(url=update_endpoint, data=updated_data)

        return order
