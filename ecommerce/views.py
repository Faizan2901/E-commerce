from django.shortcuts import render

def indexPage(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"index.html")