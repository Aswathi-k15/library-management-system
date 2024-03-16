from django.urls import path
from book import views
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('register_author',views.register),
    path('login_author',views.a_login),
    path('register_user',views.register_user),
    path('login_user',views.u_login),
    path('view_author', views.a_show),
    path('a_remove/<int:id>',views.a_remove),
    path('edit_author/<int:id>',views.a_edit),
    path('view_user', views.viewuser),
    path('u_remove/<int:id>', views.u_remove),
    path('edit_user/<int:id>', views.u_edit),
    path('add_book',views.add_book),
    path('view_book',views.viewbook),
    path('remove/<int:id>',views.remove),
    path('update/<int:id>',views.edit),
    path('home1',views.home1),
    path('home2',views.home2),
    path('',views.home,name='home'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)