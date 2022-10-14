
from django.urls import path

from . import views

urlpatterns = [
    path('',views.demov,name='demov'),
    # path('about/',views.about,name='about'),
    # path ('contact',views.contact,name='contact'),
    # path('add/',views.addition,name='addition')

]