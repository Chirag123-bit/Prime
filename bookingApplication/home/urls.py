from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("about/", views.aboutPage),
    path("details/", views.detailsPage)
]
