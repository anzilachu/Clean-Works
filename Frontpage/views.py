from django.shortcuts import render
from django.templatetags.static import static
from Core.models import ContactFormSubmission
from django.shortcuts import render, redirect

def home(request):
    image_url = static('images/slides/v1-2.jpg')

    context = {
        'image_url':image_url
    }
    return render(request,'index.html',context)


def resedential(request):
    return render(request,'residential-cleaning-services.html')

def deep_cleaning(request):
    return render(request,'deep-cleaning-services.html')

def move_in_out(request):
    return render(request,'move-in-out-cleaning.html')

def outdoor(request):
    return render(request,'outdoor-cleaning.html')

def afterparty(request):
    return render(request,'after-party-cleaning.html')

def water_tank(request):
    return render(request,'water-tank-cleaning.html')

def about(request):
    return render(request,'about.html')


def bookservice(request):
    return render(request,'contact.html')

def servicefee(request):
    return render(request,'service-fee.html')

def contact(request):
    return render(request,'contact.html')

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Create and save a new ContactFormSubmission instance
        ContactFormSubmission.objects.create(
            name=name,
            email=email,
            number=number,
            service=service,
            message=message
        )

        # Optionally, you can add additional processing here (e.g., sending emails)

        return redirect('.')  # Redirect to a success page

    return render(request, 'index.html')








