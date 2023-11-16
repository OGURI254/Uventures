from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def works(request):
    return render(request, 'projects.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    return render(request, 'service.html')
def blog(request):
    return render(request, 'blog.html')
def team(request):
    return render(request, 'team.html')
def success(request):
    return render(request, 'success.html')
def singleteam(request):
    return render(request, 'singleteam.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Retrieve all form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        subject = request.POST.get('subject')
        comments = request.POST.get('message')

        # Add your logic here to process the data and save it to the Contact model
        try:
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                subject=subject,
                comments=comments
            )
            messages.success(request, 'Details successfully processed and saved.')
            # Add any other logic or redirect as needed
            return redirect('success')  # Replace with the actual success page URL
        except Exception as e:
            messages.error(request, f'Error processing details: {str(e)}')

    return render(request, 'contact.html')




