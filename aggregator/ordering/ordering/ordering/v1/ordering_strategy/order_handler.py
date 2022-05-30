from ordering.ordering.v1.ordering_strategy.order_handler_strategy import OrderHandlerStrategy


class OrderHandler:
    def __init__(self, strategy: OrderHandlerStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    def place_order(self, request, *args, **kwargs):
        return self._strategy.place_order(request, *args, **kwargs)

    def cancel_order(self, request, *args, **kwargs):
        return self._strategy.cancel_order(request, *args, **kwargs)
