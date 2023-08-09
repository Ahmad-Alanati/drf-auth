from django.urls import path
from .views import GameListView,GameDetailView,GameCreateView,GameUpdateView,GameDeleteView,GameAllView

urlpatterns = [
    path('',GameListView.as_view(), name = 'game_list'),
    path('<int:pk>/',GameDetailView.as_view(), name = 'game_detail'),
    path('create/',GameCreateView.as_view(), name = 'game_create'),
    path('<int:pk>/update/',GameUpdateView.as_view(), name = 'game_update'),
    path('<int:pk>/delete/',GameDeleteView.as_view(), name = 'game_delete'),
    path('<int:pk>/all/',GameAllView.as_view(), name = 'game_all'),
]