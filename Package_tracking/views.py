from django.shortcuts import render, get_object_or_404,redirect
from .models import Package
from .forms import TrackingForm
from django.contrib import messages
from django.http import Http404
from django.urls import reverse




def home(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            # Redirect to track page with the tracking_id in the URL
            return redirect(reverse('track') + f'?tracking_id={tracking_id}')
    else:
        form = TrackingForm()
    
    return render(request, 'index.html', {'form': form})

def track(request):
    package = None  # Initialize package variable to None
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            try:
                # Attempt to retrieve the package with the given tracking_id
                package = Package.objects.get(tracking_id=tracking_id)
                # Render the page with the package details if found
                return render(request, 'track.html', {'package': package})
            except Package.DoesNotExist:
                # Add an error message if the tracking_id does not exist
                messages.error(request, 'Invalid tracking ID. Please check and try again.')
                return render(request, 'track.html', {'form': form})
    else:
        form = TrackingForm()  # Initialize an empty form for GET request

    # Render the template with the form (and possibly the package if it's found)
    return render(request, 'track.html', {'form': form, 'package': package})

def about(request):
    return render(request, 'about.html')

from django.core.mail import send_mail  
from django.shortcuts import render  
from django.http import HttpResponse  
from django.conf import settings  

def contact(request):  
    if request.method == 'POST':  
        name = request.POST['name']  
        email = request.POST['email']  
        subject = request.POST['subject']  
        message = request.POST['message']  

        # Compose the email  
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"  
        send_mail(subject, full_message, settings.EMAIL_HOST_USER, ['secureexpressdelivery11@gmail.com'])  

        return render(request, 'contact.html', {'sent': True})  # You can redirect or send a confirmation message  

    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def services_details(request):
    return render(request, 'services-details.html')
