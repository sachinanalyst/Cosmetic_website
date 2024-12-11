
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
    return render(request, 'store/index.html')

def services(request):
    return render(request, 'store/services.html')



def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')

        # Save the form data to the database
        contact = Contact(name=name, email=email, description=desc)
        contact.save()

        # Optionally, send a confirmation response
        return HttpResponse(f"Thank you for contacting us, {name}.<br>Your message has been saved. We will get back to you at {email}.")
    
    return render(request, 'store/contact.html')

# def contact(request):
#     return render(request, 'store/contact.html')
