from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm


def projects(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    pokemonObj = Pokemon.objects.get(id=pk)
    return render(request, 'projects/single_project.html', {'pokemon': pokemonObj})


def create_pokemon(request):
    form = PokemonForm()

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def update_pokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    form = PokemonForm(instance=pokemon)

    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES,  instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def delete_pokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('projects')
    context = {
        'pokemon': pokemon
    }
    return render(request, 'projects/delete_template.html', context)