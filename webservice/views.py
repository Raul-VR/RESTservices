from django.shortcuts import render
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . serializers import usuariosSerializer, partidasSerializer
from . models import usuarios, partidas
import sqlite3
import random
import string
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

class usuariosViewSet(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = usuariosSerializer

class partidasViewSet(viewsets.ModelViewSet):
    queryset = partidas.objects.all()
    serializer_class = partidasSerializer

def grafica(request):
    data = []
    data.append(['Jugador','Nivel','Tiempo'])
    resultados = partidas.objects.all() #select * from reto;
    url = "http://127.0.0.1:8000/api/partidas"
    header={
        "Content-Type":"application/json"
    }
    
    result = requests.get(url, headers=header)
    resultjson= result.json()
 
    max_nivel = {}

    for i in range(len(resultjson)):
        idtemp = resultjson[i]['id_usuario']
        idclean = idtemp[-2]
        nivel = resultjson[i]['nivel']
        if idclean not in max_nivel or nivel > max_nivel[idclean]:
            max_nivel[idclean] = nivel
            if len(data) > 0 and data[-1][0] == idclean:
                data[-1] = [idclean, resultjson[i]['nivel'], idclean]
            else:
                data.append([idclean, resultjson[i]['nivel'], idclean])

    print(data)
    data_formato = dumps(data) #formatear los datos en string para JSON
    myJSON = {'values':data_formato}
    return render(request,'grafica.html',myJSON)
