from django.urls import path
from CV import views


urlpatterns = [

    path('', views.home, name='home'),
    path('createprofile/', views.CreateProfile, name='createprofile'),
    path('editprofile/<str:id>/', views.EditProfile, name='editprofile'),
    path('deleteprofile/<str:id>/', views.DeleteProfile, name='deleteprofile'),



    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]
