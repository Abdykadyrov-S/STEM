from django.shortcuts import render, redirect
from .models import Courses, Buy
from apps.index.models import Settings
from apps.telegram.views import get_text

# Create your views here.
def courses(request):
    cource = Courses.objects.all()

    context = {
        "cource" : cource
    }
    return render(request, "courses.html", context)


def detail_courses(request,id):
    cource= Courses.objects.get(id=id)


    context = {
        'cource':cource
    }


    return render(request,'single-course.html',context)

def buy(request):
    settings =  Settings.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        
        review = Buy.objects.create(name = name, email = email, phone = phone)

        get_text(f"""Заявка на покупку:
Пользователь {review.name} хочет купить курс по ...
Его email {review.email},
Номер телеофона {review.phone}
""")
        return redirect("index")
        
    context ={
        'settings':settings
    }
    return render(request, 'forma.html', context)