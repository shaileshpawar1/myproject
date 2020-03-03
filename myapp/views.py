from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def StudentView(request):
    if request.method == 'POST':
        rno = request.POST.get("rno")
        name = request.POST.get("name")
        stud.objects.create(rno=rno, name=name)
        return redirect("/")
    else:
        return render(request, "insert.html")