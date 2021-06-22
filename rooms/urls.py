from django.urls import path
from . import views

app_name = "rooms"

# Funtion-based View
# urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]

# Class-based View
urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
