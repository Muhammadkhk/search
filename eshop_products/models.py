
from django.db.models import Q
from django.db import models
import os



from eshop_products_category.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"



# Create your models here.

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True).distinct()

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(type__icontains=query) |
                Q(brand__icontains=query) |
                Q(coler__icontains=query) |
                Q(size__icontains=query) |
                Q(categories__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)
    coler = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    number = models.IntegerField(default=1)

    objects = ProductsManager()

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"



class Product1(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)
    coler = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    number = models.IntegerField(default=1)

    objects = ProductsManager()

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


class Product2(models.Model):
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)
    coler = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    categories = models.ManyToManyField(ProductCategory, blank=True)
    number = models.IntegerField(default=1)

    objects = ProductsManager()

    class Meta:
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"