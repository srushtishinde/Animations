from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.loginn,name='loginn'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('register/',views.register, name='register'),
    path('authenticate/',views.authenti,name='authenti'),
    path('directory/',views.directory, name='directory'),
    path('added/',views.added,name='added'),
    path('filter/',views.filter,name='filter'),
    path('logout/',views.logout,name='logout'),
]