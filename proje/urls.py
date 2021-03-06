from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .views import *
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/', include("product.urls")),
    path('users/', include("user.urls")),
    path('your-cart/', your_cart, name="your_cart"),
   path('explore/', explore, name="explore"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)