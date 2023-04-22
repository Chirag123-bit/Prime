from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Accomodations,booking


def homepage(request):
    featured = Accomodations.objects.all()[:4]
    context = {
        "featured":featured
    }
    return render(request, "home/homepage.html",context)



def aboutPage(request):
    return HttpResponse("About Page")



def detailsPage(request,id):
    accomodation = Accomodations.objects.get(id=id)
    valid = True
    if request.user:
        bookings = booking.objects.filter(accomodation = accomodation)
        for i in bookings:
            if(i.user == request.user):
                valid = False
                break


    context = {
        "acc":accomodation,
        "valid":valid
    }

    if(request.method=="POST"):
        data = request.POST
        checkin = data.get("checkin")
        checkout = data.get("checkout")
        newBooking = booking(user=request.user,accomodation= accomodation, check_in = checkin, check_out=checkout)
        newBooking.save()
        return redirect("/")
    return render(request,"home/detailsPage.html",context)




def myBookings(request):
    bookings = booking.objects.filter(user = request.user)
    context = {
        "bookings":bookings
    }

    return render(request,"home/myBookings.html",context)