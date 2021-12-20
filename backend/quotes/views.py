from django.db.models.base import Model
from rest_framework.viewsets import ModelViewSet

from .models import Quotes
from .serializers import QuoteSerializer

class QuotesViewSet(ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer

