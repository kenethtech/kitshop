from django.shortcuts import render

def home(request):
    context = {
        "title": "index"
    }
    return render(request, 'index.html', context)
# Create your views here.
