from django.shortcuts import render,redirect
from Core.pre_fun import setip,resize_image,random_string
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'
    contacts = ContactFormSubmission.objects.filter(Status=1)
    context = {
        'page':page,
        'contacts':contacts
    }
    return render(request,'Admin/dashboard.html',context)


# @login_required
# def contact_list(request):
    
#     return render(request,'Admin/contact-list.html')


@login_required
def contact_list(request):
    page = 'contact'
    contacts = ContactFormSubmission.objects.filter(Status=1).order_by('-id')

    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = ContactFormSubmission.objects.get(id=contact_id)
        contact.Status = 0
        contact.save()
        return redirect('contact-list')
    context = {
        'contacts' : contacts,
        'page':page,
    }
    return render(request,'Admin/contact-list.html',context)

@login_required
def contact_view(request, id):
    # Fetch the contact object
    contact = ContactFormSubmission.objects.get(id=id)
    page = contact  # Assuming you want 'page' to be the same as 'contact'
    
    context = {
        'contact': contact,
        'page': page,
    }
    return render(request, 'Admin/contact-view.html', context)

