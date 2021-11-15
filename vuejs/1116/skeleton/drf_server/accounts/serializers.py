from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 입력은 받지만 출력 안함

    class Meta:
        model = User
        fields = ('username', 'password',)