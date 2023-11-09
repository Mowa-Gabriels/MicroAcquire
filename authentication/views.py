from django.shortcuts import render
from rest_framework import generics, status, views
from .serializers import (BuyerRegisterSerializer, SellerRegisterSerializer, VerifyEmailSerializer,
                           UserLoginSerializer, LogoutSerializer,
                           RequestPasswordResetSerializer, SetNewPasswordSerializer, UserSerializer)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderers


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework.permissions import IsAdminUser
from .models import User

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

@api_view(['GET'])
def apiOverview(request , format=None):

    return Response({
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        # 'list': reverse('user-list', request=request, format=format),
        # 'income': reverse('income-list', request=request, format=format)
    })

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/"
    client_class = OAuth2Client

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
  


class BuyerRegisterView(generics.GenericAPIView):

    serializer_class = BuyerRegisterSerializer
    # renderer_classes = (UserRenderers,)


    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email-buyer')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.first_name+ '\nUse the Link below to verify your Teacher Account \n'+'domain:'+absurl

        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': ' Teacher Account Verification'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class SellerRegisterView(generics.GenericAPIView):

    serializer_class = SellerRegisterSerializer
    renderer_classes = (UserRenderers,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email-seller')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.first_name+ '\nUse the Link below to verify your Student Account \n'+'domain:'+absurl

        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Student Account Verification'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class BuyerVerifyEmailView(views.APIView):
    serializer_class = VerifyEmailSerializer

    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',  type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user =  User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.is_buyer = True
                user.save()
            return Response({'email': 'Successfully Activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'email': 'Expired Token'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'email': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST) 
        


class SellerVerifyEmailView(views.APIView):
    serializer_class = VerifyEmailSerializer

    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',  type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user =  User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.is_seller = True
                user.save()
            return Response({'email': 'Successfully Activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'email': 'Expired Token'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'email': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST) 
        
class LoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request):

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_200_OK)
    

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    
    def post(self, request):

        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()   

        return Response(status=status.HTTP_200_OK)
    
class RequestPasswordReset(generics.GenericAPIView):

    serializer_class = RequestPasswordResetSerializer
    def post(self, request):

        data =request.data
        serializer = self.serializer_class(data=data)

        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            # current_site = get_current_site(request).domain
            current_site = get_current_site(request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64':uidb64, 'token':token})
            
            absurl = 'http://'+current_site+relativeLink
            email_body = 'Hi '+user.first_name+ '\nUse the Link below to reset your password. \n'+'domain:'+absurl

            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset Password'}

            Util.send_email(data)
        

        return Response({'success': "We have sent you a link to reset your password"}, status=status.HTTP_200_OK)

class PasswordTokenCheckAPIView(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                 return Response({'error': "Token is not valid. request a new one"}, status=status.HTTP_401_UNAUTHORIZED)
         
            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64':uidb64, 'token':token}, status=status.HTTP_200_OK)

               
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                 return Response({'error': "Token is not valid. request a new one"}, status=status.HTTP_401_UNAUTHORIZED)
         

class SetNewPasswordAPIView(generics.GenericAPIView):

    serializer_class =SetNewPasswordSerializer

    def patch(self, request):
        user= request.data
        serializer = self.serializer_class(data =user)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password Rest Success'}, status=status.HTTP_200_OK)
