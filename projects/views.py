
from django.http import HttpResponse
from django.shortcuts import render

pokemons = {
  "pokemon": "Squirtle",
  "type": "water",
  "number": '1'
},{
  "pokemon": "charmander",
  "type": "fire",
  "number": '2'
},{
  "pokemon": "bulbassar",
  "type": "grass",
  "number": '3'
},


def projects(request):
    context = {
        'pokemons': pokemons
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    pokemonObj = None
    for i in pokemons:
        if i['number'] == pk:
            pokemonObj = i
    return render(request, 'projects/single_project.html', {'pokemon': pokemonObj})

