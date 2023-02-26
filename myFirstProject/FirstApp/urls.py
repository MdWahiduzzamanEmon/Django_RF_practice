
from django.urls import path
from FirstApp import views

urlpatterns = [
    path('getUserInfo/', views.getUserInfo),
]

# Path: myFirstProject\FirstApp\urls.py
# Compare this snippet from myFirstProject\FirstApp\serializers.py: