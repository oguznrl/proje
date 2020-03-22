from django.shortcuts import render, redirect, get_object_or_404
from product.models import *
def home(request):
    product=Product.objects.all()
    args={
        'products':product
    }
    return render(request, "explore.html",args)
def your_cart(request):
    return render(request,"your_cart.html")

def buy_product(request,product,id):
    product = get_object_or_404(Product, id=id)
    args = {"product": product}
    return render(request,'product_buy_detail.html',args)

def product_buy_detail(request, id):
    pass




