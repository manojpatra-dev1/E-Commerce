from django.urls import path
from shop import views

urlpatterns = [
    path('', views.home, name='index'),

    path('signup/', views.signup_view, name='signup_page'),

    path('login/', views.login_view, name='login'),

    
    path('logout/', views.logout_view, name='logout'),
]