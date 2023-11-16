from django.urls import path
from Core.views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('contact-list',contact_list,name='contact-list'),
    path('contact-view/<int:id>/',contact_view, name='contact-view'),
]