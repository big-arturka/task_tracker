from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser

class CustomUserRegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'position', 'telegram_id']

        extra_kwargs = {'email':{'required':True,},
                        'first_name':{'required':True},
                        'position':{'required':True},
                        'telegram_id':{'required':True}}

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords doesnt match!')
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
                                         position=validated_data['position'], telegram_id=validated_data['telegram_id'])
        user.set_password(validated_data['password1'])
        user.save()
        return user


