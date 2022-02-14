from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def HomeView(request):
    template = "index.html"
    context = {

    }

    return render(request, template, context)

@login_required
def TodoView(request, id):
    template = "index.html"
    context = {

    }

    return render(request, template, context)