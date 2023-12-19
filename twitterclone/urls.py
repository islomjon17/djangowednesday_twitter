

from django.urls import path, include
from .  import views
urlpatterns = [
    path('', views.home, name="home"),
    
    path('profile_list/', views.profile_list, name="profile_list"),
    #profile url
    path('profile/<int:pk>', views.profile, name="profile"),
    
    path('login', views.login_user, name='login'),
    
    path('logout', views.logout_user, name='logout'),

    
    path('register_user', views.register_user, name='register'),
    
    # path(),
    
    # path(),
    
     
    
]
