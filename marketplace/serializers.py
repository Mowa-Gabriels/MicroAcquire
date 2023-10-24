
from cgitb import lookup
from marketplace.models import Startup, Tag, Technology, Industry_options, Sale_options
from authentication.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



class StartupSerializer(serializers.HyperlinkedModelSerializer):

    founders = serializers.ReadOnlyField(source='founders.email')
    id = serializers.IntegerField(read_only=True)
    industry = serializers.ChoiceField(choices=Industry_options,  style={'base_template': 'radio.html'})
    sale_type = serializers.ChoiceField(choices=Sale_options)
    


    class Meta:
        model = Startup
        fields = '__all__'
       
class StartupCreateSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Startup
        exclude = ['founders']
        



class TagSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Tag
        fields = '__all__'
        
        
class TechnologySerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Technology
        fields = '__all__'
        