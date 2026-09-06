from django.contrib import admin

from .models import Note, Document, Password, Event

admin.site.register(Note)

admin.site.register(Document)

admin.site.register(Password)

admin.site.register(Event)