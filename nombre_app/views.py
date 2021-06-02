from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

def root(request):
    return redirect(index)

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request,number1,number2):
    diferencia=number1-number2
    return HttpResponse(f"placeholder para mostrar el blog numero:{diferencia}")

def destroy(request,number):
    return redirect("/blogs")

def bjason(request):
    data={
        'titulo':'hola',
        'programa':'soy un json'                    
                        }
    return JsonResponse(data)

