from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Row, Button, ButtonHolder, Submit, Layout
from django.forms import Form, ModelForm
from django import forms
from django.urls import reverse

from customers.models import Customer

CUSTOMER_TYPE_CHOICES = [
    ('N', 'Normal'),
    ('C', 'Corporate')
]


# class CustomerCreateForm(Form):
#  customer_name = forms.CharField(
#   label="customer Full Name",
#  max_length=30
#  )
# customer_type = forms.ChoiceField(
# choices=CUSTOMER_TYPE_CHOICES
# )
class CustomerCreateForm(forms.ModelForm):
    customer_type = forms.ChoiceField(choices=CUSTOMER_TYPE_CHOICES)

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'value': 'first name'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        helper = FormHelper()

        helper.form_id = 'customer-create-form'
        helper.form_class = 'customer-create-form'
        helper.use_custom_control = True
        helper.form_tag = True
        helper.form_method = 'POST'
        helper.form_action = reverse('customer-create')

        helper.layout = Layout(
            Row(
                Div(
                    'first_name',
                    css_class='col-md-4'
                ),
                Div(
                    'middle_name',
                    css_class='col-md-4'
                ),
                Div(
                    'last_name',
                    css_class='col-md-4'
                ),

                Div(
                    'customer_type',
                    css_class='col-md-4'
                ),
                Div(
                    'age',
                    css_class='col-md-2'
                )
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-md-success'),
                Button('submit', 'cancel', css_class='btn btn-md-danger'),
                css_class='modal-footer'

            )
        )


class NextOfKinCreateForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
