from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),         # Read: Afficher tous les livres
    path('book/<int:id>/', views.book_detail, name='book_detail'),  # Read: Détail d'un livre
    path('book/new/', views.book_create, name='book_create'),       # Create: Ajouter un livre
    path('book/<int:id>/edit/', views.book_update, name='book_update'),  # Update: Modifier un livre
    path('book/<int:id>/delete/', views.book_delete, name='book_delete'),  # Delete: Supprimer un livre
]
