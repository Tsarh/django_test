from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:book_id>/', views.show, name="show"),
    path('ajouter_livre/', views.add, name="add"),
    path('maj_livre/<int:book_id>/', views.edit, name="edit"),
    path('supprimer_livre/<int:book_id>/', views.supp, name="supprimer"),
]
