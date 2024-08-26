from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Note


def index(request):
    # TODO if not existing or not int
    note = Note.objects.filter(id=int(request.GET.get("id", "1"))).first()

    if not note:
        return HttpResponse("Note was not found")

    return render(request, "notes/index.html", dict(body=note.body))


@csrf_exempt
def save(request, id):
    note = Note.objects.filter(id=int(request.GET.get("id", "1"))).first()

    if not note:
        return HttpResponse("Note was not found")
        
    note.body = request.POST.get('body', note.body)
    note.save()
    return HttpResponse("ok")
