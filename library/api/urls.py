from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.EBookListView.as_view())
]