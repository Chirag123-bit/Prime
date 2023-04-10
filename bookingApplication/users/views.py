from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.


def registerPage(request):
    if (request.method=="POST"):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    context={
        "form":form
    }
    return render(request, "users/register.html", context)





def profile(request):
  
    return render(request, "users/profile.html")