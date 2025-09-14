from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FarmerProfile, Mission, Submission, LeaderboardEntry
from django.http import JsonResponse
from .models import Badge, FarmerProfile


def watch_guide(request):
    if request.user.is_authenticated:
        profile = FarmerProfile.objects.get(user=request.user)
        badge = Badge.objects.get(name="Soil Guardian")
        if badge not in profile.earned_badges.all():
            profile.earned_badges.add(badge)
    return render(request, 'watch_guide.html')


@login_required
def missions(request):
    available_missions = Mission.objects.all()
    return render(request, 'missions.html', {'missions': available_missions})

@login_required
def submit_proof(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    if request.method == 'POST':
        proof = request.FILES['proof']
        Submission.objects.create(user=request.user, mission=mission, proof=proof)
        messages.success(request, 'Proof submitted! Awaiting verification.')
        return redirect('missions')
    return render(request, 'submit_proof.html', {'mission': mission})

def leaderboard(request):
    leaderboard = LeaderboardEntry.objects.select_related('user').order_by('-total_points')
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})

def leaderboard_api(request):
    data = [
        {
            'username': entry.user.username,
            'total_points': entry.total_points
        }
        for entry in LeaderboardEntry.objects.select_related('user').order_by('-total_points')
    ]
    return JsonResponse(data, safe=False)

def eco_farm_dashboard(request):
    if request.user.is_authenticated:
        profile, created = FarmerProfile.objects.get_or_create(user=request.user)
    return render(request, 'eco_farm_dashboard.html', {'profile': profile})

def watch_guide(request):
    if request.user.is_authenticated:
        profile, created = FarmerProfile.objects.get_or_create(user=request.user)
        badge = Badge.objects.get(name="Soil Guardian")
        if badge not in profile.earned_badges.all():
            profile.earned_badges.add(badge)
    return render(request, 'watch_guide.html')

def submit_proof(request):
    if request.user.is_authenticated:
        profile, created = FarmerProfile.objects.get_or_create(user=request.user)
    return render(request, 'submit_proof.html')

def mark_mission_complete(request):
    if request.method == "POST":
        # You can add logic here to mark the mission as completed
        messages.success(request, "Mission marked as completed!")
        return redirect('eco_farm_dashboard')
    return redirect('eco_farm_dashboard')

def eco_farm_dashboard(request):
    profile = FarmerProfile.objects.get(user=request.user)
    badges = profile.earned_badges.all()
    return render(request, 'eco_farm_dashboard.html', {'badges': badges})