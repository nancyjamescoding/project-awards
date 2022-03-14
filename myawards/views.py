from django.shortcuts import render

# Create your views here.
def awards(request):
    return render (request, 'myawards/awards.html')

def viewawards(request, pk):
    return render (request, 'myawards/myawards.html')

def addawards(request):
    return render (request, 'myawards/add.html')        