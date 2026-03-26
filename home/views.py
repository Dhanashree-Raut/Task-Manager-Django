from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from home.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User


# User - Login and Sign Up 
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 🔐 validations
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        # ✅ create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # 🔥 auto login after signup
        login(request, user)

        return redirect('task_list')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # 🔥 important
            return redirect('task_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request)   # 🔥 clears session
    return redirect('login')  # or 'home'

#  Task Related Functions

def home(request):
    # return HttpResponse("Hello, world. You're at the hoem/user index.")
    # return HttpResponse("<h1>Hello Home</h1")
    context = {
        "name" : "Dhanashree",
        "course" : "Django",
    }
    return render(request,'index.html' , context)

@login_required
def addTask(request):
    context = {'success': False}
    
    if request.method == "POST":
        # print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['M1xYxkoI5lLcgFKZRV6lT7vzhv4CmzSMlHwG0tbJDHs9wgJnl8ninWIG2oyZ4e3N'], 'title': ['Dhanashree WOek'], 'description': ['hello do this'], 'due_date': ['2026-03-16']}>
        title = request.POST['title']
        description =request.POST['description']
        duedate = request.POST['due_date']
        
        context = {'success': True}

        task = Task(title=title , desc = description , duedate = duedate )
        # print(task)    
        task.save()
    
    return render(request,'new-task.html',context )

@login_required
def listTask(request):
    # get all the task and show
    # allTask = Task.objects.all()
    allTask = Task.objects.filter(is_trash=False)
    trashTask = Task.objects.filter(is_trash=True)
    context = {'tasks' : allTask , 
               'trash_tasks':trashTask,  } 
    # context = {'tasks' : False} 
    print(allTask)
    return render(request,'list-task.html' , context)


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.desc = request.POST.get('desc')
        task.duedate = request.POST.get('duedate')
        task.save()
        return redirect('task_list')

    return redirect('task_list')  # no separate page needed

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    # task.delete()
    task.is_trash = True
    task.save()
    return redirect('task_list')

@login_required
def restore_task(request, id):
    task = get_object_or_404(Task, id=id)
    # task.delete()
    task.is_trash = False
    task.save()
    return redirect('task_list')


@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_complete = True
    task.save()
    return redirect('task_list')

