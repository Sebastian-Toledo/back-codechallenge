from django.shortcuts import render
from .models import User, Lesson
from userLessons.mapingLogic import get_all_username,get_all_users,get_all_lessons,get_name_pokemon
import requests
import json

POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon?limit=1000&offset=0'

def users_view(request,*args, **kwargs):
    print(request.user)

    users = User.objects.all()
    all_users = list(map(get_all_username,users))

    my_context = {
        'response' : all_users   
    }
    return render(request,"apiResponse.html",my_context) 

def users_view_friendship(request,*args, **kwargs):
    print(request.user)

    users = User.objects.all()
    all_users = list(map(get_all_users,users))

    my_context = {
        'response' : all_users   
    }
    return render(request,"apiResponse.html",my_context) 



def  user_view (request, username ,*args, **kwargs):

    user = User.objects.get(username = username)

    user_object = {
        'username' : username,
        'friends' : list(map(get_all_username,user.friends.all()))
    }

    my_context = {
        'response' : user_object  
    }

    return render(request,"apiResponse.html",my_context) 

def lesson_view (request, username , *args, **kwargs):
    user = User.objects.get(username = username)
    lesson = Lesson.objects.filter(user = user)

    lesson_objet = {
        'usename' : username,
        'lessons' : list(map(get_all_lessons, lesson)),
    }

    my_context = {
        'response' : lesson_objet
    }
    
    return render(request, "apiResponse.html", my_context)


def api_external_view (request, *args, **kwargs):
        
    pokemons_response =requests.get(POKEAPI_URL).text
    pokemons = json.loads(pokemons_response)
    pokemon_name = list(map(get_name_pokemon,pokemons['results']))

    my_context = {
        'response' : pokemon_name
    }

    return render(request, "apiResponse.html", my_context)

