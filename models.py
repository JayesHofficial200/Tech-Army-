from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def watch_guide(request):
    profile = FarmerProfile.objects.get(user=request.user)
    badge = Badge.objects.get(name="Soil Guardian")
    if badge not in profile.earned_badges.all():
            profile.earned_badges.add(badge)
    return render(request, 'watch_guide.html')

class Mission(models.Model):
    title = models.CharField(max_length=200)
    goal = models.TextField()
    guide_video_url = models.URLField(blank=True)
    points = models.IntegerField(default=50)
    badge = models.CharField(max_length=100, blank=True)
    is_community_challenge = models.BooleanField(default=False)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    proof = models.FileField(upload_to='proofs/')
    verified = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

class Badge(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='badges/')
    description = models.TextField()

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    earned_badges = models.ManyToManyField(Badge, blank=True)


