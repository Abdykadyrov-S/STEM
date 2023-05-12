from django.shortcuts import render
from .models import Contacts

# Create your views here.
def contacts(request):
    contact = Contacts.objects.all()

    context ={
        'contact':contact
    }
    return render(request, 'contacts.html',context)