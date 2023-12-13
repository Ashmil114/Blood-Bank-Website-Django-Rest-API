from django.shortcuts import render
from .models import Person
from .serializer import PersonSerializer
from rest_framework import viewsets
# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


