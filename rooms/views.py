from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.
def all_rooms(request):

    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    # Paginator will get 10 room_lists from the Room models.
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", {"page": rooms})
