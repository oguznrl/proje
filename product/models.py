from django.db import models
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return "%s" % (self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(verbose_name="count")
    price = models.FloatField(verbose_name="price")
    categories = models.CharField(max_length=400)
    image = models.FileField(verbose_name="image")
    company_name = models.ForeignKey(
        Company, verbose_name=("company"), on_delete=models.CASCADE)
    cart_count = models.IntegerField(null=True, blank=True, default=0)

    def _str_(self):
        return "%s" % (self.name)
    
    def categories_as_list(self):
        return self.categories.split(',')