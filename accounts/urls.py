from django.urls import path
from .views import register_view, index , logoutUser, login_view

urlpatterns = [ 
    path('register/', register_view, name='register'),
    path('', index, name='home'),
    path('logout/', logoutUser, name='logout'),
    path('login/', login_view, name='login')
]