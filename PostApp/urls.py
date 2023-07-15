from django.urls import path

from PostApp import views

urlpatterns = [
    path('post/', views.postApi),
    path('post/<int:id>/', views.postApi),
]
