from django.urls import path
from Frontpage.views import *

urlpatterns = [
    path('',home,name='home'),
]