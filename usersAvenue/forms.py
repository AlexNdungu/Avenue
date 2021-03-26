from django.forms import ModelForm
from django import forms
from .models import Order, Customer
from django.contrib.admin import widgets


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['movie','buys_types','status','date_pick','time_pick']

        

        """
        widgets = {
            'time_pick':forms.DateInput(format='%d/%m/%Y')
        }

        """
"""
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['time_pick'].widget = widgets.AdminSplitDateTime()    
        """

class AccountForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']