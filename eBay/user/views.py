from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        kullanici = request.POST.get('kullanici')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')

        
        if User.objects.filter(username = kullanici).exists():# objects.filter db ye ulaşmamızı sağlar
            messages.error(request, 'Bu Kullanıcı Adı Zaten Mevcut!')
        elif User.objects.filter(email = email).exists():
            messages.error(request, 'Bu email Zaten Mevcut!')
        elif len(password1) < 8:
            messages.error(request, 'Şifreniz EN AZ 8 KARAKTER olmalıdır!')
        elif kullanici in password1:
            messages.error(request, 'Şifreniz Kullanızı Adınız ile Benzer Olmamalıdır!')
        else:
            user = User.objects.create_user(username = kullanici, email = email, password = password1)
            user.save()
            messages.success(request, 'Başarıyla Kayıt Oldunuz')
            
            return redirect('login') 
                   
    return render(request, 'user/register.html')



def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST.get('kullanici')
        sifre = request.POST.get('password')
        
        user = authenticate(request, username = kullanici, password = sifre) # veri tabanındaki -> password
        
        if user is not None: # üstteki auth ın içindeki None
            login(request, user)
            messages.success(request, 'Başarılı bir şekilde giriş yaptınız. HOŞ GELDİNİZ!')
            return redirect('index')
        else:
            messages.error(request, 'Kullanıcı adınız veya şifreniz hatalı!')
            
    return render(request, 'user/login.html')



def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış Yaptınız!')
    return redirect('index')