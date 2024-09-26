from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('titles/<int:pk>/', views.suggested_titles, name='suggested_titles'),
    # API endpoint for title suggestions
    path('api/suggest-titles/', views.api_suggest_titles, name='api_suggest_titles'),
]
