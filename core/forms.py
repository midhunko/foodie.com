from urllib import request
from django.forms import ModelForm, Textarea, HiddenInput
from .models import Review


class ReviewForm(ModelForm):
    #user = forms.CharField(widget=forms.HiddenInput(), initial=request.user)

    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'review': Textarea(attrs={'cols': 40, 'rows': 15}),
            'user': HiddenInput()

        }
