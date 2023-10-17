
from django.urls import path
from .views import (BuyerRegisterView, SellerRegisterView,
                    BuyerVerifyEmailView,
                    SellerVerifyEmailView, 
                    LoginAPIView, PasswordTokenCheckAPIView,
                      RequestPasswordReset, SetNewPasswordAPIView, UserListView)
from rest_framework_simplejwt.views import TokenRefreshView
from authentication import views




urlpatterns = [
    
     path('overview/', views.apiOverview, name='api-overview'),

   path('register/buyer-account', BuyerRegisterView.as_view(), name='register'),
   path('register/seller-account', SellerRegisterView.as_view(), name='register'),

   path('user-list/', UserListView.as_view(), name='user-list'),
    


   path('verify-email/buyer', BuyerVerifyEmailView.as_view(), name='verify-email-buyer'), 
   path('verify-email/seller', SellerVerifyEmailView.as_view(), name='verify-email-seller'), 

   path('login/', LoginAPIView.as_view(), name='login'),  


   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('api/request-rest-email/', RequestPasswordReset.as_view(),
         name='request-rest-email'),
   
   path('api/password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(),
         name='password-reset-confirm'),

   path('api/password-reset/complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
         
]
