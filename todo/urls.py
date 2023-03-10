"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.all_todo, name='all_todo'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('change_status/<int:todo_id>', views.change_status, name='change_status'),
]
