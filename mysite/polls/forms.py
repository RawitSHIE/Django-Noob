from django import forms

from polls.models import Dayoff


class RequestModelForm(forms.ModelForm):
    class Meta:
        model = Dayoff
        exclude = ['create_by', 'approve_status']

        def clean:

