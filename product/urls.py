from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from proje.views import *

app_name = "product"
urlpatterns = [
    path('<str:product>/<int:id>',
         product_buy_detail, name="product_detail"),
    path('buy/', buy_product, name="buy"),
    path('<int:id>/add-cart', add_cart),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)