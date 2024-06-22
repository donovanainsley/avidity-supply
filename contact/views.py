from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    """ A view to render contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message delivered.\
                We\'ll responed within 2 business days.')
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_us.html', {'form': form})


def contact_success(request):
    """ A view to render contact success page """
    return render(request, 'contact/contact_success.html')