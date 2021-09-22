from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home.models import Contact

# Create your views here.
def home(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        level = request.POST['level']
        timing = request.POST['timing']
        message = request.POST['message']
        print(name, email, message) 
        ins = Contact(name=name, phone=phone, age=age, level=level, timing=timing, email=email, message=message)
        ins.save()
        messages.success(request, "Thank you for your interest in our service! we'll get back to you shortly.")
        return render(request, 'home.html', {})


    else:
        return render(request, 'home.html', {})



def eng(request):
    return render(request, 'eng.html', {})