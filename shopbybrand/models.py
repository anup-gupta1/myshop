
from django.db import models
from django.core.urlresolvers import reverse


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='brand/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shopbybrand:product_list_by_brand', args=[self.slug])


class Product(models.Model):
    brand = models.ForeignKey(Brand, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    rate = models.CharField(max_length=100, db_index=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shopbybrand:product_detail', args=[self.id, self.slug])
