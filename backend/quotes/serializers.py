from rest_framework.serializers import ModelSerializer

from .models import Quotes

class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'author', 'text']
