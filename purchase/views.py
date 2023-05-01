from django.shortcuts import render
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, "purchase/dashboard.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "purchase/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "purchase/profile.html", {"profile": profile})