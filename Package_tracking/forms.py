from django import forms
from django.core.exceptions import ValidationError

class TrackingForm(forms.Form):
    tracking_id = forms.CharField(
        max_length=12, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your tracking code. e.g. SEDX123ABC'}),
    )

    def clean_tracking_id(self):
        tracking_id = self.cleaned_data['tracking_id']
        if not tracking_id.startswith('SEDX'):
            raise ValidationError("Invalid tracking ID. It should start with 'SEDX'.")
        return tracking_id