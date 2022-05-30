from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from product.core import permissions as internal_permissions
from product.product.models import Product
from product.review.models import Review
from product.review.serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewCreateView(GenericAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [internal_permissions.HasApiKey]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()

        try:
            validated_data = serializer.validated_data
            product_id = validated_data['product'].id
            product = Product.objects.get(id=product_id)
            # already_reviewed = product.product_reviews.filter(author=request.user).exists()
            already_reviewed = product.product_reviews.filter(author=validated_data['author']).exists()
            if already_reviewed:
                return Response({'message': 'Review already exists for user!'}, status=status.HTTP_400_BAD_REQUEST)

            instance = serializer.create(validated_data)

            return Response(ReviewDetailSerializer(instance).data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response({'message': 'Something went wrong! Please try again later'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReviewListView(GenericAPIView):
    serializer_class = ReviewDetailSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Review.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()

        return Response(serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)