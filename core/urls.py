from django.urls import path
from rooms import views as room_views

# app needs to be specified because Django is going to complain.
app_name = "core"

urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]

