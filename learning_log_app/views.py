from django.shortcuts import render

# Create your views here (views roughly correspond to controllers in MVC).

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log_app/index.html')