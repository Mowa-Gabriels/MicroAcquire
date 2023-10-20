from .views import StartupListView, StartupDetailView, StartupCreateView
from django.urls import path



urlpatterns = [
    path('', StartupListView.as_view(), name='startup-list'),
    path('create/', StartupCreateView.as_view(), name='startup-create'),
    path('detail/<str:pk>/', StartupDetailView.as_view(), name='startup-detail'),
  
    
]
