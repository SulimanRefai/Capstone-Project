from django import forms
from .models import Calendar, Event

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Calendar Name"})
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time", "calendar"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Event Title"}),
            "description": forms.Textarea(attrs={"placeholder": "Event Description", "rows": 3}),
           "start_time": forms.DateTimeInput(attrs={"type": "text"}),  # type=text حتى Flatpickr يشتغل
            "end_time": forms.DateTimeInput(attrs={"type": "text"}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time:
            if end_time <= start_time:
                raise ValidationError("End time must be after the start time.")
        return cleaned_data