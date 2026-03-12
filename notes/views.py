from django.shortcuts import render, redirect,get_object_or_404
from .models import Notes 


def detail(request, id):
    note = Notes.objects.get(id=id)
    return render(request, 'detail.html', {'note': note})
    
def list_notes(request):
    notes = Notes.objects.all().order_by('-created')
    return render(request, "notes_list.html", {"notes": notes})

def add_notes(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Notes.objects.create(title=title, content=content)
        return redirect("notes:notes_list")
    return render(request, "add_notes.html")

def edit_notes(request, id):
    notes = Notes.objects.get(id=id)

    if request.method == "POST":
        notes.title = request.POST.get("title")
        notes.content = request.POST.get("content")
        notes.save()
        return redirect("notes:notes_list")

    return render(request, "edit_notes.html", {"notes": notes})
    
def delete_notes(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.delete()
    return redirect("notes:notes_list")
    
    