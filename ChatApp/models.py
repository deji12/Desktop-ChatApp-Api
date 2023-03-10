from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=255)
    key = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.room)