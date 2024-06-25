from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('star_rating', 'review_body')
        widgets = {
            'star_rating': forms.Select(choices=[(i, i) for i in range(1, 6)])
        }
