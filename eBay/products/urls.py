from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('urun/<str:productSlug>', detay, name = 'detay'),
    path('sepet/', sepet, name = 'sepet'),
    path('sepetEkle/', sepetEkle, name = 'sepetEkle'),
]