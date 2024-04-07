from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView

from .forms import WorkoutForm, AtheleteProgessForm, AtheleteForm
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
# Create your views here.

def updateOrder(request, pk):
    
     workout = Workout.objects.get(id=pk)
     form = WorkoutForm(instance=workout)
     if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('/')
     context = {'form':form}
     return render(request, 'workout_app/create_workout.html', context)

    
def WorkoutDeleteView(request, workout_id):
    
    form = WorkoutForm()
  
    workoutstuff = Workout.objects.get(pk=workout_id)
    
    if request.method =="POST":
        # delete object
        workoutstuff.delete()

        # after deleting redirect to 
        # home page
        return redirect('/')
 
    context = {'form': form}
    
    return render(request, 'workout_app/delete_workout.html', context)
def detailWorkout(request):
    # dictionary for initial data with 
    # field names as keys
    athelete_active_workout = Workout.objects.select_related('athelete_progess').all().filter(athelete_progess__is_active=True)
   
    
    # add the dictionary during initialization
   
    return render( request, 'workout_app/athelete_view.html', {'athelete_active_workout':athelete_active_workout})

def createWorkout(request, athelete_progress_id):
    form = WorkoutForm()
    athelete_progress = AtheleteProgess.objects.get(pk=athelete_progress_id)

    if request.method == 'POST':

        workout_data = request.POST.copy()
        workout_data['athelete_progress_id'] = athelete_progress_id
        form = WorkoutForm(workout_data)
        if form.is_valid():

            workout = form.save(commit=False)
            
            workout.athelete_progess = athelete_progress
            workout.save()

            return redirect('athelete-detail', athelete_progress_id)
        
    context = {'form': form}
    return render(request, 'workout_app/create_workout.html', context)


class AtheleteListView(generic.ListView):
   
   model = Athelete
  
   

class AtheleteDetailView(generic.DetailView):
    
    model = Athelete

class AtheleteDetailWorkoutView(generic.DetailView):

    model = Workout
    template_name = 'workout_app/workout_detail.html' 
    context_object_name = 'workout' 
    
def calendar_content(request):

    student_active_portfolios = Student.objects.select_related('atheleteprogress').all().filter(atheleteprogress__is_active =True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

def index(request):
# Render index.html
    athelete_active_workouts = Athelete.objects.select_related('athelete_progess').all().filter(athelete_progess__is_active =True)
    print("active workout query set", athelete_active_workouts)
    return render( request, 'workout_app/index.html', {'athelete_active_workouts':athelete_active_workouts})
