from Core.models import *

def context_processor(request):
    # Define your context variables


    project = Project.objects.filter(Status=1)

    context = {

        'project': project,
    }
    return context
