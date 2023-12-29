

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
    path('update_user', views.update_user, name='update_user'),
    # path(),
    path('update_likes/<int:pk>/', views.update_likes, name='update_likes'),
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
    
     
    
]
