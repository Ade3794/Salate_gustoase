from django.urls import path
from . import views
app_name = 'connection'

urlpatterns = [
    path('contact/', views.contact, name='contact' ),
]





