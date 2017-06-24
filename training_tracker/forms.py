from django import forms
from django.forms import formset_factory
from .models import Runner, Run, Mile
from django.contrib.auth.models import User
import html5.forms.widgets as html5_widgets

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            self.fields[field].help_text = None

class RunnerForm(forms.ModelForm):
    class Meta:
        model = Runner
        fields = ('age','hours_goal','minutes_goal','seconds_goal')

    def __init__(self, *args, **kwargs):
        super(RunnerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            self.fields[field].help_text = None


class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ['date','tot_distance','hours','minutes','seconds']
        widgets = {
            'date': html5_widgets.DateInput
        }

        labels = {
            'tot_distance':'Total distance'
        }

    def __init__(self, *args, **kwargs):
        super(RunForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            if field == "date":
                continue
            else:
                self.initial[field] = None

class MileForm(forms.ModelForm):
    class Meta:
        model = Mile
        fields = ['minutes','seconds']

    def __init__(self, *args, **kwargs):
        super(MileForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class' : 'form-control'})
            self.initial[field] = None