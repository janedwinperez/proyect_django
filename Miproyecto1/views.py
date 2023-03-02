from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def saludo(request):
    return HttpResponse("Mi primera pagina")

def dameFecha(requests):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <head>
    </head>
    <body>
    <h1>Fecha actual: %s</h1>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)

def calculaedad(request, year, edad):
    edadactual = edad
    periodo = year - 2023
    edadfutura = edadactual + periodo

    documento = """<html>
    <head>
    </head>
    <body>
    <h1>Fecha actual: %s, Edad Futura: %s</h1>
    </body>
    </html>
    """ % (edadactual, edadfutura)
    return HttpResponse(documento)

def despedida(request):
    #doc_externo = get_template("despedida.html")
    #documento = doc_externo.render({"Nombre":"Juan", "Apellido":"Perez"})
    #return HttpResponse(documento)
    return render(request, "despedida.html", {"Nombre":"Juan", "Apellido":"Perez"})