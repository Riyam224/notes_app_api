from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .serializers import NoteSerializer
from .models import Note


def notes_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return JsonResponse(serializer.data, safe=False)


# def index(request):
#     return HttpResponse("hi ")
