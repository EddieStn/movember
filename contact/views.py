from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact/contact_success.html')
