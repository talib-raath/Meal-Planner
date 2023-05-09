from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import requests
from django.views.decorators.csrf import csrf_protect
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




def generate_random_meal(request):
# List of possible meals and their calorie counts
    breakfast_choices = {
        'Oatmeal ': 100,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Avocado Toast': 250,
        'Bagel with Cream Cheese': 350,
        'Scrambled Eggs with Vegetables': 225,
        'French Toast': 400,
        'Cereal with Milk': 175,
        'Fruit Salad': 125,
        'Protein Shake': 180,
        'Egg White Omelette with Cheese': 275,
        'Breakfast Burrito': 425,
        'Waffles with Syrup': 350,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Protein Shake': 120,
        'Avocado Toast': 250,
        'Egg White Omelette': 150,
        'Greek Yogurt': 100,
        'Chia Pudding': 150,
        'Banana Nut Muffin': 200
    }
    lunch_choices = {
       'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Turkey Wrap': 300,
        'Grilled Cheese': 400,
        'Caesar Salad': 275,
        'Beef Stir-Fry': 425,
        'Chicken Quesadilla': 450,
        'Baked Potato with Toppings': 350,
        'Veggie Burger': 375,
        'Tuna Salad': 225,
        'Pizza Bagels': 300,
        'Fish Sandwich': 400,
         'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Grilled Chicken Salad': 300,
        'Chicken Caesar Wrap': 350,
        'Tuna Salad': 250,
        'Quinoa Bowl': 400,
        'Veggie Burger': 350,
        'Turkey Club Sandwich': 400
    }
    dinner_choices = {
       'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Spaghetti and Meatballs': 525,
        'Roasted Salmon': 450,
        'BBQ Ribs': 600,
        'Chicken Alfredo': 575,
        'Taco Salad': 425,
        'Beef Stroganoff': 500,
        'Lasagna': 625,
        'Grilled Steak': 450,
        'Baked Chicken': 425,
        'Shepherd\'s Pie': 475,
        'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Salmon with Roasted Vegetables': 400,
        'Turkey Chili': 350,
        'Beef Stir-Fry': 450,
        'Spaghetti Squash and Meatballs': 350,
        'Cauliflower Fried Rice': 300,
        'Baked Cod with Sweet Potato': 400
    }

    # Initialize empty list for each day of the week
    meal_plan = []
    for day in range(7):
        day_meals = {}
        day_meals['day'] = f'Day {day + 1}'

        # Choose random meals for the day
        day_meals['breakfast'] = random.choice(list(breakfast_choices.keys()))
        day_meals['lunch'] = random.choice(list(lunch_choices.keys()))
        day_meals['dinner'] = random.choice(list(dinner_choices.keys()))

        # Calculate total calories for the day's meal plan
        total_calories = (
            breakfast_choices[day_meals['breakfast']] +
            lunch_choices[day_meals['lunch']] +
            dinner_choices[day_meals['dinner']]
        )
        day_meals['total_calories'] = total_calories

        meal_plan.append(day_meals)

    # Create context dictionary with meal plan variables
    context = {'meal_plan': meal_plan}

    return render(request, 'meal_plan.html', context)

 # List of possible meals and their calorie counts
    breakfast_choices = {
        'Oatmeal': 100,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Avocado Toast': 250,
        'Bagel with Cream Cheese': 350,
        'Scrambled Eggs with Vegetables': 225,
        'French Toast': 400,
        'Cereal with Milk': 175,
        'Fruit Salad': 125,
        'Protein Shake': 180,
        'Egg White Omelette with Cheese': 275,
        'Breakfast Burrito': 425,
        'Waffles with Syrup': 350,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Protein Shake': 120,
        'Avocado Toast': 250,
        'Egg White Omelette': 150,
        'Greek Yogurt': 100,
        'Chia Pudding': 150,
        'Banana Nut Muffin': 200
    }
    lunch_choices = {
       'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Turkey Wrap': 300,
        'Grilled Cheese': 400,
        'Caesar Salad': 275,
        'Beef Stir-Fry': 425,
        'Chicken Quesadilla': 450,
        'Baked Potato with Toppings': 350,
        'Veggie Burger': 375,
        'Tuna Salad': 225,
        'Pizza Bagels': 300,
        'Fish Sandwich': 400,
         'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Grilled Chicken Salad': 300,
        'Chicken Caesar Wrap': 350,
        'Tuna Salad': 250,
        'Quinoa Bowl': 400,
        'Veggie Burger': 350,
        'Turkey Club Sandwich': 400
    }
    dinner_choices = {
       'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Spaghetti and Meatballs': 525,
        'Roasted Salmon': 450,
        'BBQ Ribs': 600,
        'Chicken Alfredo': 575,
        'Taco Salad': 425,
        'Beef Stroganoff': 500,
        'Lasagna': 625,
        'Grilled Steak': 450,
        'Baked Chicken': 425,
        'Shepherd\'s Pie': 475,
        'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Salmon with Roasted Vegetables': 400,
        'Turkey Chili': 350,
        'Beef Stir-Fry': 450,
        'Spaghetti Squash and Meatballs': 350,
        'Cauliflower Fried Rice': 300,
        'Baked Cod with Sweet Potato': 400
    }

    # Initialize empty list for each day of the week
    meal_plan = []
    for day in range(7):
        day_meals = {}
        day_meals['day'] = f'Day {day + 1}'

        # Choose random meals for the day
        day_meals['breakfast'] = random.choice(list(breakfast_choices.keys()))
        day_meals['lunch'] = random.choice(list(lunch_choices.keys()))
        day_meals['dinner'] = random.choice(list(dinner_choices.keys()))

        # Calculate total calories for the day's meal plan
        total_calories = (
            breakfast_choices[day_meals['breakfast']] +
            lunch_choices[day_meals['lunch']] +
            dinner_choices[day_meals['dinner']]
        )
        day_meals['total_calories'] = total_calories

        meal_plan.append(day_meals)

    # Create context dictionary with meal plan variables
    context = {'meal_plan': meal_plan}

    return render(request, 'meal_plan.html', context)







# Create your views here.
def demo(request):
    return render(request,"landing_page.html")
    #return HttpResponse("Hello") 

def go_to_generate_meal(request):
    return render(request, 'generate_meal.html')

def go_to_contact(request):
    return render(request, 'contact.html')

def go_to_landing_page(request):
    return render(request, 'landing_page.html')

def generate_random_meal_final(request):
 # List of possible meals and their calorie counts
    breakfast_choices = {
        'Oatmeal': 100,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Avocado Toast': 250,
        'Bagel with Cream Cheese': 350,
        'Scrambled Eggs with Vegetables': 225,
        'French Toast': 400,
        'Cereal with Milk': 175,
        'Fruit Salad': 125,
        'Protein Shake': 180,
        'Egg White Omelette with Cheese': 275,
        'Breakfast Burrito': 425,
        'Waffles with Syrup': 350,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Protein Shake': 120,
        'Avocado Toast': 250,
        'Egg White Omelette': 150,
        'Greek Yogurt': 100,
        'Chia Pudding': 150,
        'Banana Nut Muffin': 200
    }
    lunch_choices = {
       'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Turkey Wrap': 300,
        'Grilled Cheese': 400,
        'Caesar Salad': 275,
        'Beef Stir-Fry': 425,
        'Chicken Quesadilla': 450,
        'Baked Potato with Toppings': 350,
        'Veggie Burger': 375,
        'Tuna Salad': 225,
        'Pizza Bagels': 300,
        'Fish Sandwich': 400,
         'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Grilled Chicken Salad': 300,
        'Chicken Caesar Wrap': 350,
        'Tuna Salad': 250,
        'Quinoa Bowl': 400,
        'Veggie Burger': 350,
        'Turkey Club Sandwich': 400
    }
    dinner_choices = {
       'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Spaghetti and Meatballs': 525,
        'Roasted Salmon': 450,
        'BBQ Ribs': 600,
        'Chicken Alfredo': 575,
        'Taco Salad': 425,
        'Beef Stroganoff': 500,
        'Lasagna': 625,
        'Grilled Steak': 450,
        'Baked Chicken': 425,
        'Shepherd\'s Pie': 475,
        'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Salmon with Roasted Vegetables': 400,
        'Turkey Chili': 350,
        'Beef Stir-Fry': 450,
        'Spaghetti Squash and Meatballs': 350,
        'Cauliflower Fried Rice': 300,
        'Baked Cod with Sweet Potato': 400
    }

    # Initialize empty list for each day of the week
    meal_plan = []
    for day in range(7):
        day_meals = {}
        day_meals['day'] = f'Day {day + 1}'

        # Choose random meals for the day
        day_meals['breakfast'] = random.choice(list(breakfast_choices.keys()))
        day_meals['lunch'] = random.choice(list(lunch_choices.keys()))
        day_meals['dinner'] = random.choice(list(dinner_choices.keys()))

        # Calculate total calories for the day's meal plan
        total_calories = (
            breakfast_choices[day_meals['breakfast']] +
            lunch_choices[day_meals['lunch']] +
            dinner_choices[day_meals['dinner']]
        )
        day_meals['total_calories'] = total_calories

        meal_plan.append(day_meals)

    # Create context dictionary with meal plan variables
    context = {'meal_plan': meal_plan}

    return render(request, 'meal_plan.html', context)

 # List of possible meals and their calorie counts
    breakfast_choices = {
        'Oatmeal': 100,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Avocado Toast': 250,
        'Bagel with Cream Cheese': 350,
        'Scrambled Eggs with Vegetables': 225,
        'French Toast': 400,
        'Cereal with Milk': 175,
        'Fruit Salad': 125,
        'Protein Shake': 180,
        'Egg White Omelette with Cheese': 275,
        'Breakfast Burrito': 425,
        'Waffles with Syrup': 350,
        'Eggs and Toast': 200,
        'Yogurt and Granola': 150,
        'Smoothie': 200,
        'Pancakes': 300,
        'Protein Shake': 120,
        'Avocado Toast': 250,
        'Egg White Omelette': 150,
        'Greek Yogurt': 100,
        'Chia Pudding': 150,
        'Banana Nut Muffin': 200
    }
    lunch_choices = {
       'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Turkey Wrap': 300,
        'Grilled Cheese': 400,
        'Caesar Salad': 275,
        'Beef Stir-Fry': 425,
        'Chicken Quesadilla': 450,
        'Baked Potato with Toppings': 350,
        'Veggie Burger': 375,
        'Tuna Salad': 225,
        'Pizza Bagels': 300,
        'Fish Sandwich': 400,
         'Sandwich': 250,
        'Salad': 150,
        'Soup': 170,
        'Pasta': 360,
        'Burger': 475,
        'Grilled Chicken Salad': 300,
        'Chicken Caesar Wrap': 350,
        'Tuna Salad': 250,
        'Quinoa Bowl': 400,
        'Veggie Burger': 350,
        'Turkey Club Sandwich': 400
    }
    dinner_choices = {
       'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Spaghetti and Meatballs': 525,
        'Roasted Salmon': 450,
        'BBQ Ribs': 600,
        'Chicken Alfredo': 575,
        'Taco Salad': 425,
        'Beef Stroganoff': 500,
        'Lasagna': 625,
        'Grilled Steak': 450,
        'Baked Chicken': 425,
        'Shepherd\'s Pie': 475,
        'Grilled Chicken': 385,
        'Fish Tacos': 350,
        'Stir-Fry': 380,
        'Meatloaf': 485,
        'Pizza': 550,
        'Salmon with Roasted Vegetables': 400,
        'Turkey Chili': 350,
        'Beef Stir-Fry': 450,
        'Spaghetti Squash and Meatballs': 350,
        'Cauliflower Fried Rice': 300,
        'Baked Cod with Sweet Potato': 400
    }

    # Initialize empty list for each day of the week
    meal_plan = []
    for day in range(7):
        day_meals = {}
        day_meals['day'] = f'Day {day + 1}'

        # Choose random meals for the day
        day_meals['breakfast'] = random.choice(list(breakfast_choices.keys()))
        day_meals['lunch'] = random.choice(list(lunch_choices.keys()))
        day_meals['dinner'] = random.choice(list(dinner_choices.keys()))

        # Calculate total calories for the day's meal plan
        total_calories = (
            breakfast_choices[day_meals['breakfast']] +
            lunch_choices[day_meals['lunch']] +
            dinner_choices[day_meals['dinner']]
        )
        day_meals['total_calories'] = total_calories

        meal_plan.append(day_meals)

    # Create context dictionary with meal plan variables
    context = {'meal_plan': meal_plan}

    return render(request, 'meal_plan.html', context)


def generate_meal_plan_test(request):
    if request.method == 'POST':
        height = request.POST['height']
        weight = request.POST['weight']
        goal_weight = request.POST['goal-weight']
        age = request.POST['age']
        food_preferences = request.POST['food-preferences']
        allergies = request.POST['allergies']
        activity_level = request.POST['activity-level']
        meal_plan = ['Breakfast: Omelette', 'Lunch: Chicken Caesar Salad', 'Dinner: Grilled Salmon']
        context = {'meal_plan': meal_plan}
        return render(request, 'meal_plan.html', context)
    else:
        return render(request, 'meal_plan.html')





def generate_meal_plan(request):
    if request.method == 'POST':
        height = request.POST['height']
        weight = request.POST['weight']
        goal_weight = request.POST['goal-weight']
        age = request.POST['age']
        food_preferences = request.POST['food-preferences']
        allergies = request.POST['allergies']
        activity_level = request.POST['activity-level']
        
        # Requesting meal plan from Spoonacular API
        url = "https://api.spoonacular.com/mealplanner/generate"
        params = {
            "apiKey": "<0a1710ab9afc4e798836cd3bd7291aec>",
            "targetCalories": 2000, # Set the target number of calories
            "timeFrame": "day", # Set the time frame for the meal plan
            "diet": food_preferences, # Set the diet type
            "exclude": allergies # Exclude the specified ingredients
        }
        response = requests.get(url, params=params).json()
        meal_plan = response['meals']
        
        context = {'meal_plan': meal_plan}
        print (meal_plan)
        return render(request, 'meal_plan.html', context)
    else:
        return render(request, 'meal_plan.html')

