from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets, permissions
from . import serializers
from .models import MenuItem, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    pemission_classes = [permissions.IsAuthenticated]