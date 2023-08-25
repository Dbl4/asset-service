from django import forms


class AssetFilterForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    status = forms.CharField(max_length=100, required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
