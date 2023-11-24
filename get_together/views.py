from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Category, GetTogether
from .forms import GetTogetherForm


def is_facilitator(user):
    return user.profile.is_facilitator


@login_required
def get_together_list(request):
    get_togethers = GetTogether.objects.all()
    return render(request, 'get_together/get_together_list.html', {'get_togethers': get_togethers})


@login_required
def get_together_detail(request, get_together_id):
    get_together = get_object_or_404(GetTogether, pk=get_together_id)
    can_join = request.user not in get_together.participants.all() and \
               not get_together.is_full() and \
               get_together.signup_deadline > timezone.now() and \
               request.user != get_together.organizer
    return render(request, 'get_together/get_together_detail.html',
                  {'get_together': get_together, 'can_join': can_join})


@login_required
@user_passes_test(is_facilitator)
def create_get_together(request):
    if request.method == 'POST':
        form = GetTogetherForm(request.POST, request.FILES)
        if form.is_valid():
            new_category_name = form.cleaned_data.get('new_category')
            if new_category_name:
                category, created = Category.objects.get_or_create(name=new_category_name)
                get_together = form.save(commit=False)
                get_together.category = category
            else:
                get_together = form.save(commit=False)
            get_together.organizer = request.user
            get_together.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, "Get Together created successfully.")
            return redirect('get_together_detail', get_together.id)
    else:
        form = GetTogetherForm()
    return render(request, 'get_together/create_get_together.html', {'form': form})


@login_required
@user_passes_test(is_facilitator)
def edit_get_together(request, get_together_id):
    get_together = get_object_or_404(GetTogether, pk=get_together_id)
    if request.method == 'POST':
        form = GetTogetherForm(request.POST, request.FILES, instance=get_together)
        if form.is_valid():
            form.save()
            messages.success(request, "Get Together updated successfully.")
            return redirect('get_together_detail', get_together_id=get_together_id)
    else:
        form = GetTogetherForm(instance=get_together)
    return render(request, 'get_together/edit_get_together.html', {'form': form, 'get_together': get_together})


@login_required
@user_passes_test(is_facilitator)
def delete_get_together(request, get_together_id):
    get_together = get_object_or_404(GetTogether, pk=get_together_id)
    if request.method == 'POST':
        get_together.delete()
        messages.success(request, "Get Together deleted successfully.")
        return redirect('get_together_list')
    return render(request, 'get_together/delete_get_together.html', {'get_together': get_together})


@login_required
def register_for_get_together(request, get_together_id):
    get_together = get_object_or_404(GetTogether, pk=get_together_id)
    if request.method == 'POST':
        if not get_together.is_full() and get_together.signup_deadline > timezone.now():
            get_together.participants.add(request.user)
            messages.success(request, "You have successfully registered for the event.")
            return redirect('get_together_detail', get_together_id=get_together_id)
        else:
            messages.error(request, "Sorry, this get together is full or the registration deadline has passed. Please try another event.")
            return redirect('get_together_list')
    return render(request, 'get_together/register_for_get_together.html', {'get_together': get_together})


@login_required
def withdraw_from_get_together(request, get_together_id):
    get_together = get_object_or_404(GetTogether, pk=get_together_id)
    if request.method == 'POST':
        get_together.participants.remove(request.user)
        messages.success(request, "You have successfully withdrawn from the event.")
        return redirect('get_together_detail', get_together_id=get_together_id)
    return render(request, 'get_together/withdraw_from_get_together.html', {'get_together': get_together})
