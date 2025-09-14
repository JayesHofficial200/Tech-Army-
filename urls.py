from django.urls import path
from . import views

urlpatterns = [
    path('missions/', views.missions, name='missions'),
    path('submit/<int:mission_id>/', views.submit_proof, name='submit_proof'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/leaderboard/', views.leaderboard_api),
    path('eco-farm/', views.eco_farm_dashboard, name='eco_farm_dashboard'),
    path('watch-guide/', views.watch_guide, name='watch_guide'),
    path('submit-proof/', views.submit_proof, name='submit_proof'), 
    path('mark-mission-complete/', views.mark_mission_complete, name='mark_mission_complete'),
]