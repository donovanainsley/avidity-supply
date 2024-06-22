from django.shortcuts import render


def contact_us(request):
    """ A view to render contact form """
    return render(request, 'contact/contact_us.html')