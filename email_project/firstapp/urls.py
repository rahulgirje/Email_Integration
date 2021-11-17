from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomePageView,name='home'),
    path('signup/',views.SignUpPageView,name='signup'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),
]