from django.contrib import admin
from . models import notesFields

# This is needed to create a section
# in the admin panel that displays the
# specified fields
admin.site.register(notesFields)
