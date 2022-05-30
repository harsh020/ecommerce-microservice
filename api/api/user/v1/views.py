from django.db.utils import IntegrityError
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.user.models import User
from api.user.v1.serializers import UserSerializer, UserAuthSerializer, UserDetailSerializer, UserCreateSerializer, \
    UserDetailTokenizedSerializer, UserTokenizedSerializer


class UserCreateView(GenericAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()

            validated_data = serializer.validated_data
            instance = serializer.create(validated_data)

            return Response(UserTokenizedSerializer(instance).data, status=status.HTTP_201_CREATED)

        except IntegrityError as error:
            message = {
                'message': 'User with this email already exists!',
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            message = {
                'message': 'Authorization error!'
            }
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer_instance = self.get_serializer_class()

        instance = User.objects.get(id=user.id)

        return Response(serializer_instance(instance).data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data, many=False, partial=True)
        serializer.is_valid()

        validated_data = serializer.validated_data
        instance = serializer.update(user, validated_data)

        return Response(UserDetailTokenizedSerializer(instance).data, status=status.HTTP_201_CREATED)


class UserListView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer_instance = self.get_serializer_class()
        instances = serializer_instance(queryset, many=True)

        return Response(instances.data, status=status.HTTP_200_OK)


class UserAdminView(GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()

    def get(self, request, id=None):
        instance = User.objects.get(id=id)
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        user = User.objects.get(id=id)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, many=False, partial=True)
        serializer.is_valid()

        validated_data = serializer.validated_data
        instance = serializer.update(user, validated_data)

        return Response(serializer_class(instance).data, status=status.HTTP_201_CREATED)

    def delete(self, request, id=None):
        user_to_delete = User.objects.get(id=id)
        user_to_delete.user_profile.delete()
        user_to_delete.delete()

        queryset = self.get_queryset()
        serializer_instance = self.get_serializer_class()
        instances = serializer_instance(queryset, many=True)
        return Response(instances.data, status=status.HTTP_200_OK)


class UserAuthView(TokenObtainPairView):
    serializer_class = UserAuthSerializer
