from rest_framework import serializers
from . models import notesFields


# This class is needed in order to convert the specified model to JSON format
class notesSerializer(serializers.ModelSerializer):

    class Meta:
        model = notesFields
        fields = '__all__'
