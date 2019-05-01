import datetime

from django import forms

from polls.models import Dayoff


class RequestModelForm(forms.ModelForm):
    class Meta:
        model = Dayoff
        exclude = ['create_by', 'approve_status']
        widgets = {
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control'}),
        }

        error = None

        def clean(self):
            data = super.clean()

            date_start = data.get('date_start')
            date_end = data.get('date_end')

            if date_start > date_end:
                raise forms.ValidationError('invalid date input *Start date must came before End date*')
            elif date_start < datetime.datetime.now().date():
                raise forms.ValidationError('invalid date input *Start date expired*')

