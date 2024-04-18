from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def index(request):
    products = Product.objects.all()
    
    search = '' 
    if request.GET.get('q'): # arama inputu çalıştıysa
        search = request.GET.get('q')
        products = Product.objects.filter(
            Q(name__icontains = search) | # name, search i kapsıyor mu? 
            Q(kategori__name__icontains = search) 
                  
            ).distinct() #distinct :aynı bilgiye sahip ürünün birden fazla gelmesini engeller
    
    context = { # sayfada göstermek istiyorsak buraya ekle
        'products':products,
        'search':search, # search butonunda yazılanı sayfada tutma
        
    }   
    
    return render(request, 'index.html', context)


def detay(request, productSlug):
    product = Product.objects.get(slug = productSlug)
    
    context = {
        'product':product,
    }
    
    return render(request, 'detay.html', context)



def sepet(request):
    if request.user.is_authenticated:       
        sepet = Sepet.objects.filter(kullanıcı = request.user)
    else:
        return redirect('login')
    sayi = sepet.count()
    
    if 'delete' in request.POST:
        sepet.delete()
        messages.success(request, 'Ürün sepetten kaldırıldı')
        return redirect('index') 
    
    context = {
        'sepet':sepet,
        'sayi':sayi,
    }
    return render(request, 'sepet.html', context)



def sepetEkle(request):
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id = product_id)
        sepet_urun = Sepet.objects.filter(kullanıcı = request.user, urun = product).first()
        if sepet_urun:
            sepet_urun.adet += 1
            sepet_urun.save()
        else:
            Sepet.objects.create(kullanıcı=request.user,urun = product)
            
        return redirect('sepet')
    



