from django import forms
from .models import SeatBooking, Bus, Agency

class BookingForm(forms.ModelForm):
    class Meta:
        model = SeatBooking
        fields = ['seat_number','passenger_name','contact_number']

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'agency_name', 'agency_id', 'source_date', 'source', 'destination', 'source_time', 'destination_date', 'destination_time', 'total_seats']

    source_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date input
    )
    source_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M')  # HTML5 time input
    )
    destination_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date input
    )
    destination_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M')  # HTML5 time input
    )


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['name', 'contact_no', 'email', 'address', 'pincode' , 'username' , 'password' ]
