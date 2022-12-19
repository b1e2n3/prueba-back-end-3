from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from .serialiazers import InscritoSerializer
from .models import Inscrito
from serialApp.forms import FormInscrito
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class ListarInscrito(APIView):

    def get(self, request):
        estu = Inscrito.objects.all()
        serial = InscritoSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleInscrito(APIView):

    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritoSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = InscritoSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def listainscrito(request):
    perso = Inscrito.objects.all()
    data = {'inscrito': perso}
    return render(request, 'inscritos.html', data)

def index(request):
    return render(request, 'index.html')

def listarinscrito(request):
    pro = Inscrito.objects.all()
    data = {'Inscrito': pro}
    return render(request, 'listarinscrito.html', data)

def agregarinscrito(request):
    form = FormInscrito()
    if request.method == 'POST':
        form = FormInscrito(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarinscrito.html', data)

def actualizarInscrito(request, id):
    pro = Inscrito.objects.get(id = id)
    form = FormInscrito(instance=pro)
    if request.method == 'POST':
        form = FormInscrito(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarinscrito.html', data)


def eliminarInscrito(request, id):
    pro = Inscrito.objects.get(id = id)
    pro.delete()
    return redirect('/inscrito')


