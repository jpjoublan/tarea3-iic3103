from django.shortcuts import render
from django.http import HttpResponse
import requests
import ast

from .models import Greeting


# Create your views here.
def index(request):
    return render(request, "index.html")

def tarea3(request):
    query = """
            {
              allFilms {
                edges {
                  node {
                    title
                    episodeID
                    releaseDate
                    director
                    producers
                    id
                  }
                }
              }
            }
            """
    data = requests.get("https://swapi-graphql-integracion-t3.herokuapp.com/",  json={'query': query}).json()['data']['allFilms']['edges']
    return render(request, "tarea3.html", {"data": data})

def film(request):
    if request.method=='GET':
        info = request.GET.get('info')
        query = """
                {
                  film(id:"%s") {
                    title
                    episodeID
                    openingCrawl
                    director
                    producers
                    releaseDate
                    characterConnection {
                      edges {
                        node {
                          id
                          name
                        }
                      }
                    }
                    planetConnection {
                      edges {
                        node {
                          id
                          name
                        }
                      }
                    }
                    starshipConnection {
                      edges {
                        node {
                          id
                          name
                        }
                      }
                    }
                    created
                    edited



                      }
                    }
                """ % (info)

        data = requests.get("https://swapi-graphql-integracion-t3.herokuapp.com/",  json={'query': query}).json()['data']['film']
        characters_info = data['characterConnection']['edges']
        planets_info = data['planetConnection']['edges']
        starships_info = data['starshipConnection']['edges']

        return render(request, 'film.html', {"data": data, "characters": characters_info, "planets": planets_info,
                    "starships": starships_info})

def characters(request):
    if request.method=='GET':
        info = request.GET.get('info')
        # info = ast.literal_eval(info)

        query = """
                    {
              person(id:"%s") {
            		name
                height
                mass
                hairColor
                skinColor
                eyeColor
                birthYear
                gender
                homeworld {
                  id
            			name
                }

                filmConnection {
                  edges {
                    node {
                      id
                      title
                    }
                  }
                }
                starshipConnection {
                  edges {
                    node {
                      id
                      name
                    }
                  }
                }
                created
                edited


                }
            }
            """ % (info)

        data = requests.get("https://swapi-graphql-integracion-t3.herokuapp.com/",  json={'query': query}).json()['data']['person']
        films_info = data['filmConnection']['edges']
        starships_info = data['starshipConnection']['edges']
        return render(request, 'characters.html', {"data": data, "films": films_info, "starships": starships_info})

def planets(request):
    if request.method=='GET':
        info = request.GET.get('info')

        query = """
                    {
              planet(id:"%s") {
                name
                rotationPeriod
                orbitalPeriod
                diameter
                climates
                gravity
                terrains
                surfaceWater
                population
                residentConnection {
                  edges {
                    node {
                      id
                      name
                    }
                  }
                }
                filmConnection {
                  edges {
                    node {
                      id
                      title
                    }
                  }
                }
                created
                edited


            	}
            }
            """ % (info)

        data = requests.get("https://swapi-graphql-integracion-t3.herokuapp.com/",  json={'query': query}).json()['data']['planet']
        films_info = data['filmConnection']['edges']
        characters_info = data['residentConnection']['edges']

        return render(request, 'planets.html', {"data": data, "films": films_info, "characters": characters_info})

def starships(request):
    if request.method=='GET':
        info = request.GET.get('info')

        query = """
                {
                  starship(id:"%s") {
                    name
                    model
                	manufacturers
                    costInCredits
                    length
                    maxAtmospheringSpeed
                    crew
                    passengers
                    cargoCapacity
                    consumables
                    hyperdriveRating
                    MGLT
                    starshipClass
                    pilotConnection {
                      edges {
                        node {
                          id
                          name
                        }
                      }
                    }
                    filmConnection {
                      edges {
                        node {
                          id
                          title
                        }
                      }
                    }
                    created
                    edited
                	}
                }
                """ % (info)

        data = requests.get("https://swapi-graphql-integracion-t3.herokuapp.com/",  json={'query': query}).json()['data']['starship']
        films_info = data['filmConnection']['edges']
        pilots_info = data['pilotConnection']['edges']

        return render(request, 'starships.html', {"data": data, "films": films_info, "pilots": pilots_info})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
