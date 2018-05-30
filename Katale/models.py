from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.gender


class ProductType(models.Model):
    product_type = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.product_type


class Genre(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    shopper_type = models.ForeignKey(Gender, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.genre


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name


