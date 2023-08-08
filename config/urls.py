from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from coreapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('restaurant/sign_in/', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'), name='sign_in'),
    path('restaurant/sign_out/', auth_views.LogoutView.as_view(next_page='/'), name='sign_out'),
    path('restaurant/sign_up/', views.restaurant_sign_up, name='sign_up'),
    path('', views.restaurant_home, name='home'),    
]
