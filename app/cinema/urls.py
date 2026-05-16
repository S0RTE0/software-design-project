from django.urls import path
from . import views

app_name = 'cinema' 

urlpatterns = [
    path('', views.cinema_list_view, name='home'), 
    path('cinemas/', views.cinema_list_view, name='cinema_list'),
    path('cinemas/add/', views.cinema_create_view, name='cinema_create'),
    path('cinemas/<int:cinema_id>/', views.cinema_detail_view, name='cinema_detail'),

    path('sessions/', views.session_list_view, name='session_list'),
    path('sessions/<int:session_id>/', views.session_detail_view, name='session_detail'),
    
    path('sessions/<int:session_id>/buy/', views.buy_ticket_view, name='buy_ticket'),
    path('my-tickets/', views.my_tickets_view, name='my_tickets'),
]
