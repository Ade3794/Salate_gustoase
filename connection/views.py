from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm



def contact(request):
    return render(request, 'contact.html')
class ContactView(FormView):
    template_name = 'connection/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('connection')

def contact(request):

    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
                errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST('email'):
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreplay@example.com'),
            )
            return HttpResponseRedirect('connection/thanks/')
        return render(request, 'connection/contact.html', context=RequestContext(request))