from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.models import Address
from.serializer import AddressSerilazer

class AddressViewset(ModelViewSet):
    serializer_class=AddressSerilazer
    queryset=Address.objects.all()


