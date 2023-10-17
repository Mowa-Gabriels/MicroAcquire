from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from rest_framework import status




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  ['id', 'first_name', 'last_name', 'email', 'password', 'is_buyer', 'is_seller']



class BuyerRegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    
    class Meta:
        model = User
        fields = [
            "first_name", "last_name","email","password"
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not first_name.isalnum():
            raise serializers.ValidationError("First name should only contain alphanumerals")
        if not last_name.isalnum():
            raise serializers.ValidationError("Last name should only contain alphanumerals")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
    
        return user
    

class SellerRegisterSerializer(ModelSerializer):
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    
    class Meta:
        model = User
        fields = [
            "first_name", "last_name","email","password"
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')

        if not first_name.isalnum():
            raise serializers.ValidationError("First name should only contain alphanumerals")
        if not last_name.isalnum():
            raise serializers.ValidationError("Last name should only contain alphanumerals")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
    
        return user
    
    
class VerifyEmailSerializer(ModelSerializer):

    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = [
            'token'
        ]


class LoginSerializer(ModelSerializer):
    email = serializers.EmailField(min_length=6, max_length=70)
    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    tokens = serializers.CharField(
        min_length=6, read_only=True)
    first_name = serializers.CharField(
        min_length=6, max_length=70, read_only=True)
    
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'tokens',
            'password',
        ]
    


    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid Credentials')
       
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified, Contact admin')
           
        if not user.is_active:
            raise AuthenticationFailed('Account not active')
        

        return{
            'email':user.email,
            'first_name':user.first_name,
            'tokens': user.tokens()
        }

     
class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(
        min_length=6,)
    
    class Meta:
        model = User
        fields = [
            "email"
        ]

    
    # def validate(self, attrs):

    #     # email = attrs.get('email', '')
    #     email = attrs['data'].get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         user = User.objects.get(email=email)
    #         uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
    #         token = PasswordResetTokenGenerator().make_token(user)
    #         # current_site = get_current_site(request).domain
    #         current_site = get_current_site(request=attrs['data'.get('request')]).domain
    #         relativeLink = reverse('password-reset-confirm', kwargs={'uidb64':uidb64, 'token':token})
            
    #         absurl = 'http://'+current_site+relativeLink
    #         email_body = 'Hi '+user.first_name+ '\nUse the Link below to reset your password. \n'+'domain:'+absurl

    #         data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset Password'}

    #         Util.send_email(data)
            
    #     return super().validate(attrs)


class SetNewPasswordSerializer(serializers.Serializer):

    password = serializers.CharField(
        min_length=6, max_length=70, write_only=True)
    token = serializers.CharField(
        min_length=1, max_length=70, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, max_length=70, write_only=True)

    
    
    class Meta:
       
        fields = [
            "password",
            "token",
            "uidb64"
        ]
        
    def validate(self, attrs):

        try:

            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                 raise AuthenticationFailed({'error': "Reset link is not valid. request a new one"}, 401)
         
            user.set_password(password)
            user.save()
            return user
            
               
        except Exception as e:         
            raise AuthenticationFailed({'error': "Token is not valid. request a new one"}, 401)

        return super().validate(attrs)