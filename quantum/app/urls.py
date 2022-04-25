from django.urls import path
from .import views
from django.conf.urls import include
from django.contrib import admin


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.details, name='details'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('test/', views.test, name='test'),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    path('contact', views.contact, name='contact'),
]