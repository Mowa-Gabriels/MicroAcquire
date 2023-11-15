
from cgitb import lookup
from marketplace.models import Startup, Tag, Technology, Industry_options, Sale_options
from authentication.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



class StartupSerializer(serializers.HyperlinkedModelSerializer):

    founders = serializers.ReadOnlyField(source='founders.email')
    id = serializers.IntegerField(read_only=True)
    industry = serializers.ChoiceField(choices=Industry_options)
    sale_type = serializers.ChoiceField(choices=Sale_options)
    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')
    technology_used = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')  
    class Meta:
        model = Startup
        fields = '__all__'
        extra_kwargs = {
        'url' : {'view_name': 'startup-detail', 'lookup_field':'slug'}

    }
       
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
        