import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers

from . import models as m
from . import utils
from ..core import constants as c
from ..core.serializers import TMSChoiceField
from ..hr.serializers import ShortStaffProfileSerializer


class PasswordField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        if 'style' not in kwargs:
            kwargs['style'] = {'input_type': 'password'}
        else:
            kwargs['style']['input_type'] = 'password'
        super(PasswordField, self).__init__(*args, **kwargs)


class AuthSerializer(serializers.ModelSerializer):
    """
    Serializer for auth data of user
    """
    class Meta:
        model = m.User
        fields = (
            'id', 'username', 'role', 'name'
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['name'] is None:
            ret['name'] = instance.username

        if instance.role == c.USER_ROLE_ADMIN:
            ret['permissions'] = []
        elif instance.role == c.USER_ROLE_STAFF:
            ret['permissions'] = []
            if instance.permission is not None:
                for permission in instance.permission.permissions.all():
                    action = permission.action
                    for value in ret['permissions']:
                        if value['page'] == permission.page:
                            value['view'] = value['view'] or action in ['list', 'get']
                            value['edit'] = value['edit'] or action in ['create', 'update', 'delete']
                            break
                    else:
                        ret['permissions'].append({
                            'page': permission.page,
                            'view': action == 'list' or action == 'get',
                            'edit': action == 'create' or action == 'update' or action == 'delete'
                        })
        return ret


class ObtainJWTSerializer(serializers.Serializer):
    """
    Serializer class used to validate a username and password.

    'username' is identified by the custom UserModel.USERNAME_FIELD.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    role = serializers.CharField()
    device_token = serializers.CharField(required=False)

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password'),
            'role': attrs.get('role')
        }

        if all(credentials.values()):
            credentials['device_token'] = attrs.get('device_token', None)
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = utils.jwt_payload_handler(user)

                return {
                    'token': utils.jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg)


class VerificationBaseSerializer(serializers.Serializer):
    """
    Abstract serializer used for verifying and refreshing JWTs.
    """
    token = serializers.CharField()

    def validate(self, attrs):
        msg = 'Please define a validate method.'
        raise NotImplementedError(msg)

    def _check_payload(self, token):
        # Check payload valid (based off of JSONWebTokenAuthentication,
        # may want to refactor)
        options = {
            'verify_exp': False
        }
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, options=options)
        # except jwt.ExpiredSignature:
        #     msg = 'Signature has expired.'
        #     raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            msg = 'Error decoding signature.'
            raise serializers.ValidationError(msg)

        return payload

    def _check_user(self, payload):
        username = payload.get('username')

        if not username:
            msg = 'Invalid payload.'
            raise serializers.ValidationError(msg)

        # Make sure user exists
        try:
            user = m.User.objects.get(username=username)
        except m.User.DoesNotExist:
            msg = "User doesn't exist."
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = 'User account is disabled.'
            raise serializers.ValidationError(msg)

        return user


class VerifyJWTSerializer(VerificationBaseSerializer):
    """
    Check the veracity of an access token.
    """

    def validate(self, attrs):
        token = attrs['token']

        payload = self._check_payload(token=token)
        user = self._check_user(payload=payload)

        return {
            'token': token,
            'user': user
        }


class ShortUserSerializer(serializers.ModelSerializer):
    """
    Serializer for short data of User
    """
    class Meta:
        model = m.User
        fields = (
            'id', 'name', 'mobile', 'status_text'
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['name'] is None:
            ret['name'] = instance.username

        return ret


class ShortCompanyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.User
        fields = (
            'id', 'name', 'role'
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['name'] is None:
            ret['name'] = instance.username

        return ret


class ShortUserWithDepartmentSerializer(serializers.ModelSerializer):

    department = serializers.SerializerMethodField()

    class Meta:
        model = m.User
        fields = (
            'id', 'name', 'department'
        )

    def get_department(self, instance):
        ret = {}
        if instance.profile is not None:
            ret = {
                'id': instance.profile.department.id,
                'name': instance.profile.department.name
            }

        return ret


class MainUserSerializer(serializers.ModelSerializer):
    """
    Serializer for User's main data
    """
    class Meta:
        model = m.User
        fields = (
            'id', 'username', 'mobile', 'name', 'role', 'password'
        )


class DriverAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.User
        fields = (
            'id', 'username', 'mobile', 'name'
        )


class CustomerAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.User
        fields = (
            'id', 'username',
        )


class ShortUserPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.UserPermission
        fields = (
            'id', 'name'
        )


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """
    role = TMSChoiceField(choices=c.USER_ROLE)
    permission = ShortUserPermissionSerializer(read_only=True)
    driverlicense_number = serializers.SerializerMethodField()

    class Meta:
        model = m.User
        fields = '__all__'
    
    def get_driverlicense_number(self, instance):
        number = ""
        if instance.profile:
            if instance.profile.driver_license and instance.profile.driver_license.first():
                number = instance.profile.driver_license.first().number
        
        return number


class UserPermissionSerializer(serializers.ModelSerializer):

    check_items = serializers.SerializerMethodField()

    class Meta:
        model = m.UserPermission
        fields = '__all__'

    def get_check_items(self, instance):
        ret = []
        for permission in instance.permissions.all():
            action = permission.action
            for value in ret:
                if value['page'] == permission.page:
                    value['view'] = value['view'] or action == 'list' or action == 'get'
                    value['edit'] = value['edit'] or action == 'create' or action == 'update' or action == 'delete'
                    break
            else:
                ret.append({
                    'page': permission.page,
                    'view': action == 'list' or action == 'get',
                    'edit': action == 'create' or action == 'update' or action == 'delete'
                })

        return ret
