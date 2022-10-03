from rest_framework import serializers

from fullname.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserEditSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='full_name', read_only=True)

    class Meta:
        model = User
        fields = 'first_name', 'last_name'
