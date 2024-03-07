from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views
from .forms import Loginform

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',LoginView.as_view(template_name='accounts/login.html',form_class =Loginform),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]