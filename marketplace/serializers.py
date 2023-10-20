
from cgitb import lookup
from marketplace.models import Startup, Tag, Technology
from authentication.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



class StartupSerializer(serializers.ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='expense-detail', format='html')

    # founders = serializers.ReadOnlyField(source='.username')


    class Meta:
        model = Startup
        fields = '__all__'
        