from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('ajuda/' Ajuda.as_view(), name="ajuda"),
]
