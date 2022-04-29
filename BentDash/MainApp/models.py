from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Kategoriyanyn Ady')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title_one = models.CharField(max_length=255)
    title_second = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to='banner/', verbose_name='Baş sahypadaky durýan surat')

    def __str__(self):
        return self.title_one


class ProductBanner(models.Model):
    title = models.CharField(max_length=100)
    banner_image = models.ImageField(
        upload_to='banner/', verbose_name='Önümlerderdäki sahypadaky durýan surat')

    def __str__(self):
        return self.title





class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_one = models.ImageField(upload_to='product/', blank=True, null=True)
    image_second = models.ImageField(
        upload_to='product/', blank=True, null=True)
    image_three = models.ImageField(
        upload_to='product/', blank=True, null=True)
    image_fo = models.ImageField(upload_to='product/', blank=True, null=True)
    description = models.TextField()



    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    title_second = models.CharField(max_length=255)
    title_check_1 = models.CharField(max_length=50)
    title_check_2 = models.CharField(max_length=50)
    title_check_3 = models.CharField(max_length=50)
    title_check_4 = models.CharField(max_length=50)
    about = models.TextField()
    banner = models.ImageField(upload_to='about/', blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    image = models.ImageField(upload_to='contact/')
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    about_us = models.TextField()
    image_top = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.address


class Stars(models.Model):
    name = models.CharField(max_length=75)
    bill = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("-created_at",)
