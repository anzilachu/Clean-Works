from Core.models import ContactFormSubmission

def context_processor(request):
    # Define your context variables


    form_submissions = ContactFormSubmission.objects.filter(Status=1)

    context = {

        'form_submissions': form_submissions,
    }
    return context
