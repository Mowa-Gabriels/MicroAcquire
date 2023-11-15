
from django.urls import path, include
from .views import (BuyerRegisterView, SellerRegisterView,
                    BuyerVerifyEmailView,
                    SellerVerifyEmailView, 
                    LoginAPIView, LogoutAPIView, PasswordTokenCheckAPIView,
                      RequestPasswordReset, SetNewPasswordAPIView, UserViewSet, LogoutAPIView,)
from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework_simplejwt.views import TokenBlacklistView
from authentication import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'user', UserViewSet)




urlpatterns = [
    
    path('', include(router.urls)),
    
     path('overview/', views.apiOverview, name='api-overview'),

   path('register/buyer-account', BuyerRegisterView.as_view(), name='register'),
   path('register/seller-account', SellerRegisterView.as_view(), name='register'),

# #    path('user-list/', UserListView.as_view(), name='user-list'),
#    path('user/<str:slug>/', UserDetailView.as_view(), name='user-detail'),
#     path('user/profile/<str:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    


   path('verify-email/buyer', BuyerVerifyEmailView.as_view(), name='verify-email-buyer'), 
   path('verify-email/seller', SellerVerifyEmailView.as_view(), name='verify-email-seller'), 

   path('login/', LoginAPIView.as_view(), name='login'),  
   path('logout/', LogoutAPIView.as_view(), name='logout'),  


   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
   
   path('api/request-rest-email/', RequestPasswordReset.as_view(),
         name='request-rest-email'),
   
   path('api/password-reset/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(),
         name='password-reset-confirm'),

   path('api/password-reset/complete/', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
         
]

