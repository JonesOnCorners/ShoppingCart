from django.shortcuts import render, render_to_response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from display.models import Item
from display.serializers import ItemSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser 
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.

 #View to handle student creation          
class ItemDisplayView(generics.ListCreateAPIView):
    renderer_classes = [ TemplateHTMLRenderer ]
    template_name = 'index.html'
    def get(self, request):
        queryset = Item.objects.all()
        return Response({'items':queryset})
    #queryset =  Item.objects.all()
    #serializer_class = ItemSerializer
    
        
    
    
class ItemCreateView(generics.ListCreateAPIView):
    #queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def get_queryset(self):
        return Item.objects.all()