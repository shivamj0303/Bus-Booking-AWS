from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, SeatBooking, Agency
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, BusForm, AgencyForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# BOTO3
import boto3
from django.shortcuts import render
from boto3.dynamodb.conditions import Key, Attr
# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# Access DynamoDB tables
bus_table = dynamodb.Table('Buses')
seat_booking_table = dynamodb.Table('SeatBookings')
agency_table = dynamodb.Table('Agencies')

#BOTO3

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def after_registeration(request):
    return render(request, 'after_registeration.html')


def search_bus(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        if source and destination:
            buses = Bus.objects.filter(source__icontains=source, destination__icontains=destination)
        else:
            buses = Bus.objects.all()
        return render(request, 'search_bus.html', {'buses': buses})
    return render(request, 'search_bus.html')

@login_required
def book_seat(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            seat_number = form.cleaned_data['seat_number']
            if SeatBooking.objects.filter(bus=bus, seat_number=seat_number).exists():
                form.add_error(None, 'Seat is already booked.')
            else:
                SeatBooking.objects.create(user=request.user, bus=bus, seat_number=seat_number)
                return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'book_seat.html', {'bus': bus, 'form': form})


@login_required
def register_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            # Directly save the form since Django should handle time parsing
            form.save()
            return redirect('home')
        else:
            # If form is invalid, return form with errors to the template
            return render(request, 'register_bus.html', {'form': form})
    else:
        form = BusForm()
    return render(request, 'register_bus.html', {'form': form})


@login_required
def register_agency(request):
    if request.method == 'POST':
        form = AgencyForm(request.POST)
        if form.is_valid():
            agency = form.save(commit=False)  # Save the form without committing to the database
            agency.save()  # Now save it to generate the ID
            return redirect('agency_id', agency_id=agency.id)  # Redirect to the new view with the agency's ID
    else:
        form = AgencyForm()
    return render(request, 'register_agency.html', {'form': form})

def agency_id(request, agency_id):
    agency = get_object_or_404(Agency, id=agency_id)
    return render(request, 'agency_id.html', {'agency': agency})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')
