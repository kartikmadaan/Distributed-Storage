from rest_framework import serializers
from .models import User, BusService, HotelService

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'email', 'type', 'token', 'activated', )

class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusService
        fields = ('id', 'name', 'route', 'timing', 'price', 'bus_number', 'is_ready', 'provider', 'seats', 'boarding_point', )

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelService
        fields = ('id', 'name', 'city', 'area', 'check_in', 'check_out', 'price', 'is_ready', 'provider', 'rooms', 'address', )
