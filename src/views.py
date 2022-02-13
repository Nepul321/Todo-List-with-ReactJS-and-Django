from django.shortcuts import render

def HomeView(request):
    template = "index.html"
    context = {

    }

    return render(request, template, context)

def TodoView(request, id):
    template = "index.html"
    context = {

    }

    return render(request, template, context)