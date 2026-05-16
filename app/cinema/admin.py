from django.contrib import admin
from .models import Cinema, Session, Hall, Ticket

admin.site.register(Cinema)
admin.site.register(Session)
admin.site.register(Hall)
admin.site.register(Ticket) 
