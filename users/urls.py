from django.urls import path
from. import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='users/home.html'), name="login"),
    path('register/',views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
