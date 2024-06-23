from datetime import date

from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError

from .models import Fixture


class FixtureForm(ModelForm):
    class Meta:
        model = Fixture
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number","min":"1", "max":"80"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Fixtures cannot be in the past")
        return d