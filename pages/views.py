from django.shortcuts import render,redirect
from .models import feed
from .forms import newfeed

def HomePageView(request):
    fdata = feed.objects.all()
    return render(request, 'home.html', {'fdata' : fdata})
# Create your views here.

def edit(request):

    form = newfeed()
    if request.method == 'POST':
        form = newfeed(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'edit.html', {'form' : form})
