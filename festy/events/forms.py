from django import forms
from .models import Event
  
# creating a form 
class EventCreationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)


    class Meta:
        fields = ['event_name','description', 'event_start_timestamp', 'event_end_timestamp',
                'event_location_lon','event_location_lat','event_capacity']
        model = Event