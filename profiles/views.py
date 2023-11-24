from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile


@login_required
def user_profile(request):
    """ Displays the user's profile. """
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'form': form})


@login_required
def toggle_facilitator_status(request):
    profile = request.user.profile
    profile.is_facilitator = not profile.is_facilitator
    profile.save()
    return redirect('profile')  # Redirect back to the profile page
