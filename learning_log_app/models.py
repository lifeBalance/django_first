from tabnanny import verbose
from django.db import models


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # This nested class (some weird shit) allows us to define the plural of
    # Entry as Entries and not Entrys (that would be the default).
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representation of the entry."""
        # Return up to the first 50 characters of the text attribute.
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text
