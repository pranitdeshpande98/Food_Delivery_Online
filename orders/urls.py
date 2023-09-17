from django.urls import path
from .import views

urlpatterns = [
    path('place_order/',views.placeorder,name="placeorder"),
]