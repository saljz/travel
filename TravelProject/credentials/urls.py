from.import views
from django.urls import path

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    #path('',views.demo,name='demo'),
    #path('add/',views.addition,name='addition')
    #path('about/',views.about,name='about')
]
