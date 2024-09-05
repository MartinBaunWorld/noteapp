from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Note


def note_all(request):
    # TODO if not int it blows up
    note = Note.objects.filter(id=int(request.GET.get("id", "1"))).first()

    if not note:
        return HttpResponse("Note was not found")

    return render(request, "note_all.html", dict(body=note.body))


@csrf_exempt
def note_edit(request, id):
    # TODO if not int it blows up
    note = Note.objects.filter(id=int(request.GET.get("id", "1"))).first()

    if not note:
        return HttpResponse("Note was not found")
        
    note.name = request.POST.get('name', note.name)
    note.body = request.POST.get('body', note.body)
    note.save()
    return HttpResponse("ok")
