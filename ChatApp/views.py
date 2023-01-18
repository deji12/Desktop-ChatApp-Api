from django.shortcuts import render, redirect
from .models import Room, Message
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['POST'])
def HomePage(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return Response({'success': 'Room exists'})

        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return Response({'success': 'Room created successfully'})

    # return render(request, 'index.html')

@api_view(['POST', 'GET'])
def MessageView(request, room_name, username):

    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages= Message.objects.filter(room=get_room).order_by('-date')

    serializer = ChatSerializer(get_messages, many=True)
    
    return Response({"success": "room gotten", "messages": serializer.data})