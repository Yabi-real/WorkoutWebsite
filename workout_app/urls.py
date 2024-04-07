from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.

path('', views.index, name='login'),
path('', views.index, name='logout'),
path('', views.index, name='index'),
path('main_menu/', views.AtheleteListView.as_view() , name= 'atheletes'),
path('athelete_detail/<int:pk>/', views.AtheleteDetailView.as_view(), name='athelete-detail'),
path('create_workout/<int:athelete_progress_id>', views.createWorkout, name="create-workout"),
path('delete_workout/<str:workout_id>/', views.WorkoutDeleteView, name="delete-workout"),

path('workout_see/<int:pk>/', views.AtheleteDetailWorkoutView.as_view(), name="view-workout"),
path('workout_view/', views.detailWorkout, name="list-workout"),
path('update_workout/<str:pk>/', views.updateOrder, name="update-workout"),
]
