from django.shortcuts import render
from django.templatetags.static import static
from django.shortcuts import render, redirect

def home(request):
    image_url = static('images/slides/v1-2.jpg')

    context = {
        'image_url':image_url
    }
    return render(request,'index.html',context)





