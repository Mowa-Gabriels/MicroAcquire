from django.shortcuts import render
from marketplace.models import *
from rest_framework import generics
from marketplace.serializers import StartupSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class StartupListView(generics.ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]
    #authentication_classes = [SessionAuthentication, BasicAuthentication]

class StartupCreateView(generics.CreateAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [IsAuthenticated]
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
   

    def perform_create(self, serializer):
        return serializer.save(founders=self.request.user)
 
    def get_queryset(self):
        return self.queryset.filter(founders=self.request.user)
    



class StartupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer