from django import forms    # Import the forms module

from .models import Topic   # Import the Topic model

class TopicForm(forms.ModelForm):
    # The nested Meta class tells Django which model to base the form on.
    class Meta:
        model = Topic
        fields = ['text']       # This form will only have a text input field.
        labels = {'text': ''}   # The label will be empty (no label).