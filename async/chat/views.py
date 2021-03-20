from django.shortcuts import render


def index(requeust):
    return render(requeust, 'index.html', {})


def room(requeust, room_name):
    ctx = {
        'room_name': room_name
    }
    return render(requeust, 'chatroom.html', ctx)
