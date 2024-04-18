# Generated by Django 4.2.10 on 2024-04-03 12:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, verbose_name='Ürün İsmi')),
                ('content', models.TextField(verbose_name='Ürün Açıklaması')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Resim')),
                ('price', models.IntegerField(default=0, verbose_name='Ürn Fiyatı')),
                ('slug', models.SlugField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]