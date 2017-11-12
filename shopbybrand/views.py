from django.shortcuts import render, get_object_or_404
from .models import Brand, Product
from cart.forms import CartAddProductForm


def product_list(request, brand_slug=None):
    brand = None
    categories = Brand.objects.all()
    products = Product.objects.filter(available=True)
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
    cart_product_form = CartAddProductForm()
    return render(request, 'shopbybrand/product/list.html', {'brand': brand,
                                                      'brands': brands,
                                                      'cart_product_form': cart_product_form,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shopbybrand/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})





def store(request, brand_slug=None):
    brand = None
    brands = Brand.objects.all()
    products = Product.objects.filter(available=True)
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
    cart_product_form = CartAddProductForm()
    return render(request, 'shopbybrand/store.html', {'brand': brand,
                                                      'brands': brands,
                                                      'cart_product_form': cart_product_form,
                                                      'products': products})