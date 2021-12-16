from django.urls import path
from .views import *


urlpatterns = [
    path('users/', UserCategoryListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]