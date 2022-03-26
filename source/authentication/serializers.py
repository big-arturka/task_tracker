from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.db import transaction
from .models import CustomUser
from django.contrib.auth.models import Group
from .services import mailing

class CustomUserRegisterSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    user_type = serializers.ChoiceField(choices=(
        ('Common', 'Commom'),
        ('Staff', 'Staff')
    ), write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'position', 'telegram_id', 'user_type']

        extra_kwargs = {'email':{'required':True,},
                        'first_name':{'required':True},
                        'position':{'required':True},
                        'telegram_id':{'required':True}}

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords doesnt match!')
        return data

    @transaction.atomic
    def create(self, validated_data):
        user_type = validated_data['user_type']
        user = CustomUser.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
                                         position=validated_data['position'], telegram_id=validated_data['telegram_id'])
        user.set_password(validated_data['password1'])
        if user_type == 'Staff':
            user.is_active = False
            group = Group.objects.get(name = 'Staff')
            user.groups.add(group)
            mailing(user.email)

        else:
            group = Group.objects.get(name = 'Common User')
            user.groups.add(group)
        user.save()
        return user



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'profile_image', 'position', 'telegram_id']

    #TODO
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.position = validated_data.get('position', instance.position)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


