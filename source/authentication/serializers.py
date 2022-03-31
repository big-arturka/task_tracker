from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'check_password', 'first_name', 'position', 'telegram_id']

        extra_kwargs = {'email':{'required':True,},
                        'first_name':{'required':True},
                        'position':{'required':True},
                        'telegram_id':{'required':False},
                        'password':{'write_only':True},
                        }


    def create(self, validated_data):
        if validated_data['password'] != validated_data['check_password']:
            raise serializers.ValidationError('Passwords doesnt match!')
        user = CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'],
                                         position=validated_data['position'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


