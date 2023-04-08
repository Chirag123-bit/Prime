from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.


def registerPage(request):
    form = RegistrationForm()
    context={
        "form":form
    }
    return render(request, "users/register.html", context)