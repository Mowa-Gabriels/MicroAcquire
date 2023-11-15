
from rest_framework import viewsets
from django.shortcuts import render
from marketplace.models import *
from rest_framework import generics
from marketplace.serializers import (StartupSerializer,StartupCreateSerializer,
                                     TagSerializer, TechnologySerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from marketplace.utils import IsOwnerOrReadOnly
from django_filters import rest_framework as filters

from rest_framework import filters




# class StartupListView(generics.ListAPIView):
#     queryset = Startup.objects.all()
#     serializer_class = StartupSerializer
#     permission_classes = [AllowAny]
#     #authentication_classes = [SessionAuthentication, BasicAuthentication]

# class StartupCreateView(generics.CreateAPIView):
#     queryset = Startup.objects.all()
#     serializer_class = StartupCreateSerializer
#     permission_classes = [IsAuthenticated,]
#     #authentication_classes = [SessionAuthentication, BasicAuthentication]
   

#     def perform_create(self, serializer):
#         return serializer.save(founders=self.request.user)
 
#     def get_queryset(self):
#         return self.queryset.filter(founders=self.request.user)
    

# class StartupDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Startup.objects.all()
#     serializer_class = StartupSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     lookup_field = "pk"


# class TagView(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [AllowAny]

# class TechnologyView(generics.ListCreateAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer
#     permission_classes = [AllowAny]


# class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     permission_classes = [AllowAny]
#     lookup_field = "pk"

# class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer
#     permission_classes = [AllowAny]
#     lookup_field = "pk"



from django_filters import rest_framework as filters
class StartupFilter(filters.FilterSet):

    rev_min_price = filters.NumberFilter(field_name="revenue", lookup_expr='gte')
    rev_max_price = filters.NumberFilter(field_name="revenue", lookup_expr='lte')
    min_price = filters.NumberFilter(field_name="profit", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="profit", lookup_expr='lte')

    class Meta:
        model = Startup
        fields = ['company_name', 'industry']


class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [AllowAny]
    # search_fields = ['company_name', 'industry', 'country','tag__name', 'technology_used__name']
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StartupFilter


    def get_serializer_class(self):
        if self.action == 'create':
            return StartupCreateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(founders=self.request.user)

    # def get_queryset(self):
    #     user = self.request.user
    #     return self.queryset.filter(founders=user)
    
 



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [AllowAny]

