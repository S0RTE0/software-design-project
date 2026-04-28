from django.shortcuts import render, get_object_or_404, redirect
from .models import Cinema, Session, Hall
from .forms import CinemaForm

def cinema_list_view(request):
    cinemas = Cinema.objects.all()
    context = {
        "title": "Cinemas List",
        "cinemas": cinemas,
    }
    return render(request, 'cinema/cinema_list.html', context=context)

def cinema_detail_view(request, cinema_id: int):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    context = {
        "title": f"Cinema Details - {cinema.name}",
        "cinema": cinema,
    }
    return render(request, 'cinema/cinema_detail.html', context=context)

def session_list_view(request):
    sessions = Session.objects.all()
    context = {
        "title": "Sessions Schedule",
        "sessions": sessions,
    }
    return render(request, 'cinema/session_list.html', context=context)

def session_detail_view(request, session_id: int):
    session = get_object_or_404(Session, id=session_id)
    context = {
        "title": f"Session Details - {session.name}",
        "session": session,
    }
    return render(request, 'cinema/session_detail.html', context=context)

def cinema_create_view(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('cinema:cinema_list') 
    else:
        form = CinemaForm() 

    context = {
        "title": "Add New Cinema",
        "form": form,
    }
    return render(request, 'cinema/cinema_form.html', context=context)
