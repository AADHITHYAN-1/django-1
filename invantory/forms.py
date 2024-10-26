from django import forms
from .models import buy  # Import the Product model

class buyForm(forms.ModelForm):  # Class name should be in PascalCase and use forms.ModelForm
    class Meta:
        model = Product  # Reference the Product model
        fields = '__all__'  # Include all fields from the model
