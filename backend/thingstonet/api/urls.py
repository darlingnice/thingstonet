from django.urls import path
from . import views


urlpatterns = [
     path('user/<int:id>',views.get_user,name="get_user"),
     path('users',views.get_users,name="get_users"),
     path('add-user',views.add_user,name="add_user"),
     path('add-staff-user',views.add_staff_user,name="add_staff_user"),
     path('add-deveolper',views.add_developer,name="add_developer"),  
     path('login',views.login_view,name="login"),  
     path('logout',views.logout_view,name='logout'),
     path('test',views.test,name="test")
]