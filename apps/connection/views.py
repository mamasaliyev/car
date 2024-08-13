from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import ContactForm
from django.http import HttpResponse

from .models import Contact


# def submit_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = form.save()
#             return HttpResponse(f'Thank you, {contact.name}! Your message has been received.')
#         else:
#             return HttpResponse('Invalid form submission')
#     else:
#         form = ContactForm()
#     return render(request, 'contact/contact.html', {'form': form})


class ContactListView(View):
    template_name = 'contact/contact-list.html'

    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, self.template_name, {'contacts': contacts})


class ContactCreateView(LoginRequiredMixin, View):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.info(request, 'Thank you, Your message has been received!')
            return redirect('contact-list')
        return render(request, self.template_name, {'form': form})
