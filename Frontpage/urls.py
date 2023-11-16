from django.urls import path
from Frontpage.views import *

urlpatterns = [
    path('',home,name='home'),
    path('residential/',resedential,name='resedential'),
    path('deep-cleaning/',deep_cleaning,name='deep_cleaning'),
    path('move_in_out/',move_in_out,name='move_in_out'),
    path('outdoor/',outdoor,name='outdoor'),
    path('afterparty/',afterparty,name='afterparty'),
    path('water_tank/',water_tank,name='water_tank'),
    path('about/',about,name='about'),
    path('bookservice/',bookservice,name='bookservice'),
    path('service_fee/',servicefee,name='servicefee'),
    path('contact/',contact,name='contact'),
    path('submit_contact_form/', submit_contact_form, name='submit_contact_form'),
]