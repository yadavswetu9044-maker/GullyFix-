from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('issue/<int:id>/', views.issue_detail, name='issue_detail'),
    path('stats/', views.stats_view, name='stats'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('contact/', views.contact_view, name='contact'),
]