from django import forms
from .models import Product

""" class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ] """

class RawProductForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-className second-name",
        "rows": 10,
        "cols": 120,
        "id": "new-id"
    }))
    price = forms.DecimalField(initial=100.00)

# Form validation methods
class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", 
    widget=forms.TextInput(attrs={
        "placeholder": "Your Title"
    }))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "new-className second-name",
        "rows": 10,
        "cols": 120,
        "id": "new-id"
    }))
    price = forms.DecimalField(initial=100.00)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "ash" in title:
            raise forms.ValidationError("This is not a valid title") 
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title") 
        return title
            