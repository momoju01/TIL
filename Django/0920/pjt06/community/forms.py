from django import forms
from .models import Review

# ModelFrom
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

