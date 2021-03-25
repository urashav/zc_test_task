from django.urls import path
from messages_api import views


app_name = 'messages_api'

urlpatterns = [
    path('message/create', views.MessageCreateView.as_view()),
    path('all/', views.MessageListView.as_view()),
    path('message/detail/<int:pk>/', views.MessageDetailView.as_view())
]
