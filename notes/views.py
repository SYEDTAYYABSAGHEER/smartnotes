from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes': all_notes})

class DetailListView(ListView):
    model = Notes
    context_object_name = 'note'

# def details(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Notes does not exist')
#     return render(request, 'notes/details.html',{'note':note})

