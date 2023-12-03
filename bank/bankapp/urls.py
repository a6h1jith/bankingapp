from django.urls import path
from bankapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('welcome/',views.welcome,name='welcome'),
    path('form/',views.form,name='form'),
    path('message/',views.message,name='message')
]