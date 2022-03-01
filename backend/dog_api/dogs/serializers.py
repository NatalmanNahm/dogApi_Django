from rest_framework import serializers
from .models import Dog
from .models import Breed


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            '',
        )
        model = Dog