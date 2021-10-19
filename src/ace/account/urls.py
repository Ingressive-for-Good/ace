from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, login, profile


urlpatterns = [
	# path('profile/', user_views.profile, name='profile'),
	# path('register/', user_views.register, name='register'),
	# path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
	path('signup/', register, name='signup'),
	path('login/', login, name='login'),
	path('user/profile/', profile, name='profile'),
]


