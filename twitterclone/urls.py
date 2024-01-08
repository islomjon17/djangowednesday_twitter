

from django.urls import path, include
from .  import views
urlpatterns = [
    path('', views.home, name="home"),
    # profile url
    path('profile_list/', views.profile_list, name="profile_list"),
    #profile url
    path('profile/<int:pk>', views.profile, name="profile"),
    # login url
    path('login', views.login_user, name='login'),
    # logout url
    path('logout', views.logout_user, name='logout'),

    # register user url
    path('register_user', views.register_user, name='register'),
    # update url
    path('update_user', views.update_user, name='update_user'),
    # updates like url
    path('update_likes/<int:pk>/', views.update_likes, name='update_likes'),
    # post share url
    path('post_share/<int:pk>/', views.post_share, name='post_share'),
    
     
    
]
