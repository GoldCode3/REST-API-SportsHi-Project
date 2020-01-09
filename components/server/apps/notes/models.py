from django.db import models
from django.utils import timezone


# This class is created to list the fields that should be included
class notesFields(models.Model):
    id = models.IntegerField(primary_key=True)
    note_content = models.CharField(max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)

    # This method returns the content of the field
    def __str__(self):
        return self.id
