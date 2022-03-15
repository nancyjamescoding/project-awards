from email.mime import image
from django.shortcuts import render, redirect
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
    projects=Project.objects.all()

    if request.method =='POST':
        data =request.POST
        image =request.FILES.get('image')
        author = request.user

        projects= Project.objects.create(
            caption = data.get('caption', ""),
            image = image, 
            author = author,
        )
        return redirect('awards')
    return render (request, 'myawards/add.html', {'projects': projects})        