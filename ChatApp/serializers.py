from rest_framework import serializers
from ChatApp import models

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Room
        fields = '__all__'