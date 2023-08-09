from django.shortcuts import render
from .models import Game
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .serializers import GameSerializer,GameCreateSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameCreateSerializer
    permission_classes = [IsAuthenticated]

class GameUpdateView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]

class GameDeleteView(RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]

class GameAllView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]