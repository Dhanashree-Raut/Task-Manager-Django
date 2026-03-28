from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from home.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from .forms import SignUpForm


# User - Login and Sign Up 
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            user = form.save()
            login(request, user)          # auto-login after signup
            return redirect('home')       # change 'home' to your home URL name
        else:
            print(form.errors) 
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form})
 
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

#  Task Related Functions -----------------------------------------------------

def home(request):
    
    slider_data = [
    {
        "title": "Manage Tasks Without Stress",
        "desc": "Plan, organize, and track your daily tasks effortlessly with a clean and powerful interface.",
        "img": "https://images.unsplash.com/photo-1554774853-aae0a22c8aa4?q=80&w=1600",
        "btn_text": "Get Started"
    },
    {
        "title": "Never Miss a Deadline",
        "desc": "Stay on top of your work with due dates, reminders, and real-time progress tracking.",
        "img": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?q=80&w=1600",
        "btn_text": "Explore Features"
    },
    {
        "title": "Work Better Together",
        "desc": "Collaborate with your team, share tasks, and communicate seamlessly in one place.",
        "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=1600",
        "btn_text": "Start Collaborating"
    }
]
    
    features = [
        {
            "title": "Task Management",
            "img": "https://images.unsplash.com/photo-1554774853-aae0a22c8aa4?q=80&w=1000",
            "desc": "Easily create, organize, and manage all your daily tasks in one place.",
            "points": [
                "Quickly add tasks with minimal effort",
                "Add detailed descriptions for better clarity",
                "Set due dates to stay on schedule",
                "Edit and update tasks anytime",
                "Organize tasks based on priority",
                "Keep everything structured and easy to find"
            ]
        },
        {
            "title": "Delete & Recycle",
            "img": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?q=80&w=1000",
            "desc": "A safe and reliable system to manage deleted tasks without losing important data.",
            "points": [
                "Delete tasks safely without permanent loss",
                "Move deleted tasks to recycle bin",
                "Restore tasks anytime when needed",
                "Permanently delete unwanted tasks",
                "Prevent accidental data loss",
                "Keep your workspace clean and organized"
            ]
        },
        {
            "title": "Task Status Tracking",
            "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=1000",
            "desc": "Track the progress of your tasks and stay productive every day.",
            "points": [
                "Mark tasks as complete when finished",
                "Reopen tasks by marking them incomplete",
                "Track progress visually and clearly",
                "Focus on pending and important tasks",
                "Monitor daily productivity easily",
                "Stay consistent with your workflow"
            ]
        }
    ]
    
    upcoming_features = [
        {
            "title": "Task Sharing",
            "img": "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?q=80&w=1000",
            "desc": "Easily share tasks with others and collaborate in real-time.",
            "points": [
                "Share tasks with friends or teammates",
                "Assign responsibilities to specific users",
                "Collaborate on shared tasks efficiently",
                "Get real-time updates on changes",
                "Control access and permissions",
                "Improve team coordination effortlessly"
            ]
        },
        {
            "title": "Team Collaboration",
            "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1000",
            "desc": "Work together in teams and manage projects more efficiently.",
            "points": [
                "Create teams for projects or departments",
                "Assign tasks to team members easily",
                "Track team progress in one dashboard",
                "Distribute workload efficiently",
                "Collaborate on shared goals",
                "Improve productivity with teamwork"
            ]
        },
        {
            "title": "Team Comments & Chat",
            "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=1000",
            "desc": "Communicate directly within tasks and keep conversations organized.",
            "points": [
                "Add detailed comments on each task",
                "Have real-time team discussions",
                "Tag team members for quick updates",
                "Maintain conversation history",
                "Share important notes and feedback",
                "Improve communication within teams"
            ]
        }
    ]
    
    return render(request, 'index.html', {
        'slider_data': slider_data,
        'features': features,
        'upcoming_features': upcoming_features
    })
    
    
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

        task = Task( author=request.user,  title=title , desc = description , duedate = duedate )
        # print(task)    
        task.save()
    
    return render(request,'new-task.html',context )

@login_required
def listTask(request):
    # get all the task and show
    # allTask = Task.objects.all()
    
    # --- Without user 
    # allTask = Task.objects.filter(is_trash=False)
    # trashTask = Task.objects.filter(is_trash=True)
    
    # With user filter 
    allTask = Task.objects.filter(author=request.user, is_trash=False)
    trashTask = Task.objects.filter(author=request.user, is_trash=True)

    context = {'tasks' : allTask , 
               'trash_tasks':trashTask,  } 
    # context = {'tasks' : False} 
    print(allTask)
    return render(request,'list-task.html' , context)


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, author=request.user)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.desc = request.POST.get('desc')
        task.duedate = request.POST.get('duedate')
        task.save()
        return redirect('task_list')

    return redirect('task_list')  # no separate page needed

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, author=request.user)
    # task.delete()
    task.is_trash = True
    task.save()
    return redirect('task_list')

@login_required
def restore_task(request, id):
    task = get_object_or_404(Task, id=id, author=request.user)
    # task.delete()
    task.is_trash = False
    task.save()
    return redirect('task_list')

@login_required
def complete_task(request, id):
    task = get_object_or_404(Task, id=id, author=request.user)
    task.is_complete = True
    task.save()
    return redirect('task_list')

@login_required
def remove_complete_task(request, id):
    task = get_object_or_404(Task, id=id, author=request.user)
    task.is_complete = False
    task.save()
    return redirect('task_list')

