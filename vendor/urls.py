from . import views
from django.urls import path,include
from accounts import views as AccountViews


urlpatterns = [
    path('profile/',views.vprofile,name='vprofile'),
    path('',AccountViews.vendorDashboard,name='vendor'),
    path('menu-builder/',views.menu_builder,name = 'menu_builder'),
    path('menu-builder/category/<int:pk>/',views.fooditems_by_category,name="fooditems_by_category"),

    ## Category CRUD Operations
    path('menu-builder/category/add/',views.add_category,name="add_category"),
    
]