# from django.shortcuts import render, get_object_or_404
# from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import notesFields
from . serializers import notesSerializer
import json



# This class based view is used for the get and post methods
class notesList(APIView):

    # Returns all specified fields in model
    def get(self, request):
        # This variable is used to store all objects
        notesVar = notesFields.objects.all()
        # This serializer is used to convert to JSON format
        serializer = notesSerializer(notesVar, many=True)
        # This returns the data as a response in JSON format
        return Response(reversed(serializer.data))

    # Submitting all of the data
    def post(self, request):
        if request.method == 'POST':
            payload = json.loads(request.body)
            id = payload['id']
            note_content = payload['note_content']
            note = notesFields(id=id, note_content=note_content)
            note.save()
            response = json.dumps([{'id':note.id, 'note_content':note.note_content}])
        return HttpResponse(response, content_type='application/json')