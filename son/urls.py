from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('login_page/',views.login_page,name="login"),
    path('register_page/' ,views.register_page ,name="register"),
    path('logout_page',views.logout_page,name="logout"),
    path('update_task/<str:pk>',views.update_task,name="update_task"),
    path('delete_task/<str:pk>',views.delete_task,name="delete_task"),
]