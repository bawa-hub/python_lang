from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': 'learn python'},
    {'id': 2, 'name': 'learn django'},
    {'id': 3, 'name': 'learn frontend'}
]


def home(request):
    # return HttpResponse("Hello world!")
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    # return HttpResponse("Room")
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
