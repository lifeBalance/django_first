from django.shortcuts import render
from .models import Topic

# Create your views here (views roughly correspond to controllers in MVC).

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log_app/index.html')

def topics(request):
    """Show all topics."""
    # Pull the list of topics from the model.
    topics = Topic.objects.order_by('date_added')
    # Define a context dictionary, and hang the topics there as an attribute.
    context = {'topics': topics}
    return render(request, 'learning_log_app/topics.html', context)