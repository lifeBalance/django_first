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

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # Query to select a topic using the value captured in the url (/<int:topic_id>/)
    topic = Topic.objects.get(id=topic_id)
    # Query to get all the entries in the topic, ordered by date.
    entries = topic.entry_set.order_by('-date_added')
    # Build a context dictionary with the topic and its list of entries.
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_log_app/topic.html', context)