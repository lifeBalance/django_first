from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank form.
        form = UserCreationForm() # empty form
    else:
        # Process data in the submitted form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # Save the username and the hashed password to DB. Return user.
            new_user = form.save()
            # Log in the user, and redirect to home page.
            login(request, new_user) # Log in the user above.
            return redirect('learning_log_app:index')
    
    # Display a blank or invalid form (if we didnd't return in the statement above)
    context = {'form': form}
    return render(request, 'registration/register.html', context)