from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Cinema, Session, Hall, Ticket
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
    today = timezone.now().date()
    sessions_today = cinema.sessions.filter(start_time__date=today)
    
    context = {
        "title": f"Cinema Details - {cinema.name}",
        "cinema": cinema,
        "sessions_today": sessions_today,
    }
    return render(request, 'cinema/cinema_detail.html', context=context)

def session_list_view(request):
    today = timezone.now().date()
    sessions = Session.objects.filter(start_time__date=today)
    context = {
        "title": "Today's Sessions Schedule",
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

@login_required 
def buy_ticket_view(request, session_id: int):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        seat_number = Ticket.objects.filter(session=session).count() + 1
        Ticket.objects.create(
            user=request.user,
            session=session,
            seat_number=seat_number
        )
        return redirect('cinema:my_tickets') 
    return redirect('cinema:session_detail', session_id=session.id)

@login_required
def my_tickets_view(request):
    tickets = request.user.tickets.all() 
    context = {
        "title": "My Electronic Tickets",
        "tickets": tickets,
    }
    return render(request, 'cinema/my_tickets.html', context=context)
