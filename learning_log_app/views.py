from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here (views roughly correspond to controllers in MVC).


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_log_app/index.html")


# If the user is not logged in, it's redirected to the login page.
@login_required
def topics(request):
    """Show all topics."""
    # Pull the list of topics from the model.
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    # Define a context dictionary, and hang the topics there as an attribute.
    context = {"topics": topics}
    return render(request, "learning_log_app/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # Query to select a topic using the value captured in the url (/<int:topic_id>/)
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    # Query to get all the entries in the topic, ordered by date.
    entries = topic.entry_set.order_by("-date_added")
    # Build a context dictionary with the topic and its list of entries.
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_log_app/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # For non-POST request we instantiate  a blank form.
        form = TopicForm()
    else:
        # Instantiate the form passing the body of the POST request in the const.
        form = TopicForm(data=request.POST)
        # Validate that all fields are present, and that they conform to
        # the attributes of the Topic model (text max. length 200 chars.)
        if form.is_valid():
            # We need to add ownership to topic before saving it to DB
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_log_app:topics")

    # If we didn't return in the else > if clause, display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_log_app/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
     # Fetch topic with a given id from the collection of Topics.
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # For non-POST requests instantiate a blank form.
        form = EntryForm()
    else:
        # For POST requests we have to process the submitted data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Get the new instance of the form without saving it to the DB.
            new_entry = form.save(commit=False)
            # Assign the topic to the topic attribute of this object.
            new_entry.topic = topic
            # Now we can save it to the DB.
            new_entry.save()
            return redirect('learning_log_app:topic', topic_id=topic_id)
    # If we didn't return in the statement above, display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_log_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic # Store the topic of the entry in 'topic'
    # Protect the edit_entry page so that only owner can edit her topics.
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # For GET requests, pre-fill the form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # Process the data submitted in the POST request.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_log_app:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_log_app/edit_entry.html', context)