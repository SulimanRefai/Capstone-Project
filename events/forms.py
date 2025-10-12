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
            "start_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
