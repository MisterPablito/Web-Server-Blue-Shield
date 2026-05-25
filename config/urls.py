from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from social import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', views.register_error, name='register_error'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]