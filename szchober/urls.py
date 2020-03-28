from django.urls import path
from szchober import views

app_name = 'szchober'

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('become-a-rider/', views.become_rider, name='become-a-rider'),
    path('become-a-driver/', views.become_driver, name='become-a-driver'),
    path('my-account-rider/', views.myAccount_rider, name='my_rider_account'),
    path('find-a-lift/', views.find_lift, name='find_a_lift'),
    path('my-account-driver/', views.myAccount_driver, name='my_driver_account'),
    path('about-us/', views.about, name='about-us'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
]
