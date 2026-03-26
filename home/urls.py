
from django.contrib import admin
from django.urls import path , include
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('newtask', views.addTask, name='new-task'),
    path('listtask', views.listTask, name='task_list'),
    # path('view/<int:id>/', views.view_task, name='view_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('restore/<int:id>/', views.restore_task, name='restore_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
    
    # Login and signupp
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
