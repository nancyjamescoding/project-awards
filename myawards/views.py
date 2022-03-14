from django.shortcuts import render
from . models import Project

# Create your views here.
def awards(request):
    projects=Project.objects.all()
    context = { 'projects': projects}
    return render (request, 'myawards/awards.html', context)

def viewawards(request, pk):
    projects=Project.objects.get(id=pk)
    return render (request, 'myawards/myawards.html',{'projects': projects})

def addawards(request):
    return render (request, 'myawards/add.html')        