from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    path('',views.index, name='inicio' ),
    path('registro/', views.registro, name="registro"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]