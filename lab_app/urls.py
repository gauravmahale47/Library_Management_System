from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('list', book_list),
    path('register',registration,name='register'),
    path('login',mylogin,name='login'),
    path('logout',mylogout,name='logout'),
    path('add',add,name='add'),
    path('edit/<int:id>',edit,name='edit'),
    path('update',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]