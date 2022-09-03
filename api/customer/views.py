from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView

from api.customer.serializer import CustomerSerializer
from customers.models import Customer


class CustomerCreateAPIView(CreateAPIView):
    serializer_class = CustomerSerializer


class CustomerListAPIView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
