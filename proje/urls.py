from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from proje.views import home,buy_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('product/<str:product>/<int:id>', buy_product),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)