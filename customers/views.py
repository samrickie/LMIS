from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from .form import CustomerCreateForm, NextOfKinCreateForm
from .models import Customer


# Create your views here.

class CustomerListView(ListView):
    queryset = Customer.objects.all()
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'
    success_url = '/customers'

    def get_queryset(self):
        qs = Customer.objects.all()
        return qs


class CustomerCreateView(CreateView):
    template_name = 'customer/customer_create.html'
    form_class = CustomerCreateForm
    success_url = '/customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['welcome_message'] = 'welcome to CRDB MS'
        context['next_of-kin_form'] = NextOfKinCreateForm()

        return context

    def form_valid(self, form):
        data = form.cleaned_data
        customer = form.save(commit=False)
        last_name = str(data.get('last_name')).upper()
        customer.last_name = last_name
        customer.save()
        if customer:
            context = {'message': 'Customer saved successful'}
            return HttpResponseRedirect(reverse('customer-list'), context)
        else:
            context = {'message': 'customer save failed'}
            return render(self.request, self.template_name, context)


class CustomerDetailsView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/customer_update.html'
    fields = ['first_name', 'middle_name', 'last_name', 'age']
    success_url = '/customers'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    success_url = '/customers'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
