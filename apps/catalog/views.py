from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Logo, Car, Contract
from .forms import LogoForm, CarForm, ContractForm

# Logo Views
class LogoListView(ListView):
    model = Logo
    template_name = 'logo_list.html'
    context_object_name = 'logos'

class LogoDetailView(DetailView):
    model = Logo
    template_name = 'logo_detail.html'
    context_object_name = 'logo'

class LogoCreateView(CreateView):
    model = Logo
    form_class = LogoForm
    template_name = 'logo_form.html'
    success_url = reverse_lazy('logo_list')

class LogoUpdateView(UpdateView):
    model = Logo
    form_class = LogoForm
    template_name = 'logo_update.html'
    success_url = reverse_lazy('logo_list')

class LogoDeleteView(DeleteView):
    model = Logo
    template_name = 'logo_delete.html'
    success_url = reverse_lazy('logo_list')

# Car Views
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')

# Contract Views
class ContractListView(ListView):
    model = Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'

class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contract_detail.html'
    context_object_name = 'contract'

class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_form.html'
    success_url = reverse_lazy('contract_list')

class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_update.html'
    success_url = reverse_lazy('contract_list')

class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contract_delete.html'
    success_url = reverse_lazy('contract_list')
