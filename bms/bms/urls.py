from django.contrib import admin
from django.urls import path
from pustak.views import book,delete_book,update_book,register_page,login_page,logout_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',book),
    path('delete_book/<id>/',delete_book,name="delete_book"),
    path('update_book/<id>/',update_book,name="update_book"),
    path('register/',register_page,name="register_page"),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name="logout_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)