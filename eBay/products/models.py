from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Kategori(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key = True, db_index = True, unique = True, default = uuid.uuid4, editable = False)# uuid4 -> random id
    name = models.CharField(max_length = 150, verbose_name = 'Ürün İsmi')
    content = models.TextField(('Ürün Açıklaması'))   
    kategori = models.ForeignKey(Kategori, on_delete = models.SET_NULL, null = True)   
    image = models.ImageField(upload_to="products/", verbose_name= "Resim")
    price = models.IntegerField(default = 0, verbose_name = "Ürün Fiyatı")
    slug = models.SlugField(null = True, blank = True, editable = False) # blank -> boş bırakılmasını kabul ediyor, null=True -> boş kaldığında null olacak
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    
    def save(self, *args, **kwargs):# isim değiştirip kaydedince slug a kaydetsin
        
        self.slug = f"{slugify(self.name.replace('ı','i'))}-{str(self.id)[:8]}"  #! slug ismi aynı olan ürünler karışmasın diye id kullandım
        
        super().save(*args, **kwargs) #miras almak için
    
    def __str__(self):
        return self.name # object1 olarak gelmesin diye
    
    class Meta:# admin panelini etkiliyor
        verbose_name_plural = "Ürünler"
        verbose_name = "Ürün"


class Sepet(models.Model):
    kullanıcı = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Sepete Ekleyen' )
    urun = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = 'Eklenen Ürün')
    adet = models.IntegerField(default = 1, verbose_name = 'Adet')
    satinAlmaTarihi = models.DateTimeField(auto_now_add = True)
    
    
    
    
    def __str__(self):
        return self.urun.name
    
    
    