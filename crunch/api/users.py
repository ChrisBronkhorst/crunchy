from rest_framework import serializers, viewsets, response, status, views, renderers, permissions
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser)

    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
