

from django.urls import path, include
from .  import views
urlpatterns = [
    path('', views.home, name="home"),
    
    path('profile_list/', views.profile_list, name="profile_list"),
    
    # path(),
    
    # path(),
    
    # path(),
    
    # path(),
    
    # path(),
    
    # path(),
    
     
    
]
