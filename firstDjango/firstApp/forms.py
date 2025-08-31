from django import forms
from .models import ChaiVarity   # correct model name

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label='Select chai variety'
    )
