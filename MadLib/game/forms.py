

from django import forms
from .models import Story
from .models import Input
from .models import UserInput


class GamePrepForm(forms.Form):
    def __init__(self, inputs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for obj in inputs:
            self.fields[obj.input_name] = forms.CharField(label=obj.input_name, required=True)
