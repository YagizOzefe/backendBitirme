from .models import *

def get_categories(request):
    kategoriler = Kategori.objects.all()
    return {'kategoriler':kategoriler}
