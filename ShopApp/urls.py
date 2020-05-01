from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete1/', views.delete1, name='delete1'),
]