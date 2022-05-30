from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from api.user.models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(source='is_staff')

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'is_admin', 'date_joined',)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('is_deleted', 'created', 'modified', 'user')


class UserTokenizedSerializer(UserSerializer):
    access = serializers.SerializerMethodField()

    def get_access(self, user):
        return str(RefreshToken.for_user(user).access_token)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'is_admin', 'date_joined', 'access')


class UserDetailSerializer(UserSerializer):
    profile = UserProfileSerializer(many=False, required=False, source='user_profile', partial=True)

    def get_profile(self, user):
        profile_instance = user.user_profile
        return UserProfileSerializer(profile_instance).data

    def update(self, user, validated_data):
        if 'user_profile' in validated_data:
            profile_data = validated_data.pop('user_profile')

            profile = UserProfile.objects.get(id=user.user_profile.id)
            serializer = UserProfileSerializer(data=profile_data, partial=True)
            serializer.is_valid()
            profile = serializer.update(profile, serializer.validated_data)

            user.user_profile = profile
        user = super().update(user, validated_data)

        if validated_data.get('is_staff', None) is not None:
            user.is_staff = True
            user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'is_admin', 'profile', 'date_joined')


class UserDetailTokenizedSerializer(UserDetailSerializer):
    access = serializers.SerializerMethodField()

    def get_access(self, user):
        return str(RefreshToken.for_user(user).access_token)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'profile', 'is_admin', 'date_joined', 'access')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active', 'id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user)
        return user


class UserAuthSerializer(TokenObtainPairSerializer):
    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        serializer = UserTokenizedSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        del data['refresh']

        return data


