from django.urls import path

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('quotes', QuotesViewSet)

urlpatterns = router.urls