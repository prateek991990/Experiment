from django.urls import path, include
from. import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_home, name = 'all_home'),
    path('<int:blog_id>/', views.details, name = 'details')
    ]
