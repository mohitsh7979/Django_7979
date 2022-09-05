from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from.models import Address

class AddressSerilazer(ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'