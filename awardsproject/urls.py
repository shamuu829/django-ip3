from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView, LoginView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('awardsapp.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), {"next_page": '/'}),
    path('accounts/',include('django_registration.backends.one_step.urls')),

]