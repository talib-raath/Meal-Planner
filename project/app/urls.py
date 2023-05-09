from django.urls import path
from . import views

urlpatterns = [
    path('',views.go_to_landing_page),
    path('landing',views.go_to_landing_page),
    path('Meal_Plan',views.generate_meal_plan),
    path('generate_meal',views.go_to_generate_meal),
    path('contact',views.go_to_contact),
    path('Random_meal',views.generate_random_meal),    
]

