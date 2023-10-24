# from .views import (StartupListView, StartupDetailView,
#                      StartupCreateView,TagDetailView, TechnologyDetailView)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StartupViewSet, TagViewSet, TechnologyViewSet


router = DefaultRouter()
router.register(r'startups', StartupViewSet)
router.register(r'tags', TagViewSet)
router.register(r'technologies', TechnologyViewSet)

urlpatterns = [
     path('', include(router.urls)),

    # path('', StartupListView.as_view(), name='startup-list'),
    # path('create/', StartupCreateView.as_view(), name='startup-create'),
    # path('detail/<str:pk>/', StartupDetailView.as_view(), name='startup-detail'),

    # path('tag/detail/<str:pk>/', TagDetailView.as_view(), name='tag-detail'),
    # path('technology/detail/<str:pk>/', TechnologyDetailView.as_view(), name='technology-detail'),


]
