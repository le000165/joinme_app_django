from django.urls import path, include
from . import views

urlpatterns = [
    # localhost:/, loging page
    path('', views.user_login, name='user_login'),
    # localhost:/, sign up form page
    path('signup/', views.signup_form, name='signup_user'),
    # localhost:/activity, loading a list of activity
    path('activity_list/', views.activity_list, name='activity_list'),
    # localhost:/activity, loading an activity details
    path('activity_list/details=<int:id>/', views.activity_details, name='activity_details'),
    # localhost:/joinme/create, get and post request for insert operation
    path('create/', views.activity_form, name='activity_create'),
]
