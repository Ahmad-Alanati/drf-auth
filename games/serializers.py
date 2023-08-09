from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name','price','description','released_date']

class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','name','purchaser','price','description','released_date']