from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('base/',views.user_base,name='base'),
    path('about/',views.user_about,name='about'),
    path('feedback/',views.user_feedback,name='feedback'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('addevent/',views.user_addevent,name='addevent'),
]
