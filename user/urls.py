from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from  .views import * 


app_name = "user"

urlpatterns = [

    path('login/', loginUser, name='login'),

    path('logout/', logoutUser, name='logout'),

    path('signup/', register, name='signup'),

    path('profile/<str:username>', profile),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)