from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
from urllib.parse import urlencode
from .models import *
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from datetime import date
def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def cus_register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        hname=request.POST.get('hname') 
        district=request.POST.get('district')
        street=request.POST.get('street')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        pin=request.POST.get('pin')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if customer_reg.objects.filter(email=email).exists() or staff_reg.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'cus_register.html', {'msg': 'Email already exists. Please use a different email.'})
       
        cus=customer_reg(fname=fname,hname=hname,district=district,street=street,phone=phone,gender=gender,dob=dob,pin=pin,email=email,password=password)
        cus.save()
        log=tbl_login(email=email,password=password,user_type='customer',status='Active')
        log.save()
        return render(request,"index.html", {'message':'Succesfully Registered'})
    else:
        return render(request,"cus_register.html")
    
    
def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request,'admin/index.html')

    elif customer_reg.objects.filter(email=email,password=password).exists():
        userdetails=customer_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['cuid'] = userdetails.id
            request.session['cuname'] = userdetails.fname
            request.session['cuemail'] = email

            return render(request,'index.html')
        
    elif staff_reg.objects.filter(email=email,password=password).exists():
        userdetails=staff_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['sid'] = userdetails.id
            request.session['sname'] = userdetails.name
            request.session['semail'] = email

            return render(request,'admin/index.html')
   
    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

#admin

def dash(request):
    return render(request,'admin/index.html')

def staff_register(request):
    return render(request,"admin/addstaff.html")
def add_staff_register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        district=request.POST.get('district')
        hname=request.POST.get('hname')
        gender=request.POST.get('gender')
        pin=request.POST.get('pin')
        password=request.POST.get('password')
        if customer_reg.objects.filter(email=email).exists() or staff_reg.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'admin/addstaff.html', {'msg': 'Email already exists. Please use a different email.'})
        
        cus=staff_reg(name=name,district=district,hname=hname,phone=phone,gender=gender,pin=pin,email=email,password=password)
        cus.save()
        log=tbl_login(email=email,password=password,user_type='staff',status='Active')
        log.save()
        return render(request,"admin/index.html", {'message':'Succesfully Registered'}) 
    

def view_staff(request):
    staff=staff_reg.objects.all()
    return render(request,'admin/viewstaff.html',{'result':staff})

def removestaff(request,id):
    staff=staff_reg.objects.get(id=id)
    staff.delete()
    return redirect(view_staff)

def view_cus(request):
    staff=customer_reg.objects.all()
    return render(request,'admin/viewcustomer.html',{'result':staff})


def removecustomer(request,id):
    staff=customer_reg.objects.get(id=id)
    staff.delete()
    return redirect(view_cus)

def add_flights(request):
    if request.method == "POST":
        flight_name = request.POST.get('flight_name')
        flight_model = request.POST.get('flight_model')
        flight_maxcap = int(request.POST.get('flight_maxcap'))
        business_cap = int(request.POST.get('business_cap'))
        first_cap = int(request.POST.get('first_cap'))
        economy_cap = int(request.POST.get('economy_cap'))
        year = request.POST.get('year')

        # Calculate the total capacity
        total_capacity = business_cap + first_cap + economy_cap

        # Check if the total capacity exceeds the maximum capacity
        if total_capacity > flight_maxcap:
            return render(request, "admin/index.html", {'message': 'capacity exceeds maximum capacity.'})

        cus = tbl_flight(flight_name=flight_name, flight_maxcap=flight_maxcap, business_cap=business_cap,
                         flight_model=flight_model,first_cap=first_cap, economy_cap=economy_cap,year=year, status='Active')
        cus.save()
        return render(request, "admin/index.html", {'message': 'Successfully Added Flight'})
    else:
        return render(request, "admin/add_flights.html")



def view_flights(request):
    flights=tbl_flight.objects.all()
    return render(request,"admin/view_flights.html",{'result':flights})


def edit_flight(request,id):
    if request.method=="POST":
        flight_name=request.POST.get('flight_name')
        flight_model=request.POST.get('flight_model')
        flight_maxcap=request.POST.get('flight_maxcap')
        business_cap=request.POST.get('business_cap')
        first_cap=request.POST.get('first_cap')
        economy_cap=request.POST.get('economy_cap')
        year=request.POST.get('year')
       
        cus=tbl_flight(flight_name=flight_name,flight_maxcap=flight_maxcap,business_cap=business_cap,flight_model=flight_model,first_cap=first_cap,economy_cap=economy_cap,year=year,status='Active',id=id)
        cus.save()
        return render(request,"admin/index.html",{'message':'Succesfully Edited Flight'})
    else:
        flight=tbl_flight.objects.get(id=id)
        return render(request,"admin/edit_flights.html",{'result':flight})

def remove_flight(request,id):
    filght=tbl_flight.objects.get(id=id)
    filght.delete()
    return redirect(view_flights)

def add_route(request):
    if request.method=="POST":
        starting_point=request.POST.get('starting_point')
        destination=request.POST.get('destination')
        distance=request.POST.get('distance')
        stop=request.POST.get('stop')
        if not stop:
            stop = 'Direct'
     
        cus=tbl_route(starting_point=starting_point,destination=destination,distance=distance,stop=stop)
        cus.save()
        return render(request,"admin/index.html",{'message':'Succesfully Added Route'})
    else:
        return render(request,"admin/add_route.html")
    
def view_route(request):
    flights=tbl_route.objects.all()
    return render(request,"admin/view_route.html",{'result':flights})

#staff

def route_assign(request):
    if request.method=="POST":
        flight_id = request.POST.get('flight_id')
        route_id = request.POST.get('route_id')
        departure_date = request.POST.get('departure_date')
        arrival_date = request.POST.get('arrival_date')
        departure_time = request.POST.get('departure_time')
        arrival_time = request.POST.get('arrival_time')
        first_class_rate = request.POST.get('first_class_rate')
        business_class_rate = request.POST.get('business_class_rate')
        normal_class_rate = request.POST.get('normal_class_rate')
        infant_rate = request.POST.get('infant_rate')

        # Check if the selected flight is already allocated for the same date and route
        existing_allocation = tbl_routeassign.objects.filter(
            flight_id=flight_id,
            route_id=route_id,
            departure_date=departure_date
        ).exists()

        if existing_allocation:
            return render(request, "admin/index.html", {'message': 'Flight already allocated for the same date and route'})

        # Check if the entered time conflicts with existing allocations
        time_conflict = tbl_routeassign.objects.filter(
            Q(flight_id=flight_id, departure_date=departure_date, departure_time__range=(departure_time, arrival_time)) |
            Q(flight_id=flight_id, departure_date=departure_date, arrival_time__range=(departure_time, arrival_time))
        ).exists()

        if time_conflict:
            return render(request, "admin/index.html", {'message': 'Time conflict with existing allocation'})

        # Check if the entered time is between the departure_time and arrival_time
        if arrival_time < departure_time:
            return render(request, "admin/index.html", {'message': 'Arrival time cannot be before departure time'})

        # If all checks pass, insert into tbl_routeassign
        cus = tbl_routeassign(
            flight_id=flight_id,
            route_id=route_id,
            departure_date=departure_date,
            arrival_date=arrival_date,
            departure_time=departure_time,
            arrival_time=arrival_time,
            first_class_rate=first_class_rate,
            business_class_rate=business_class_rate,
            normal_class_rate=normal_class_rate,
            infant_rate=infant_rate,
            status='Active'
        )
        cus.save()
        return render(request, "admin/index.html", {'message': 'Successfully Added Route Allocation'})
    else:
        routes = tbl_route.objects.all()
        flights = tbl_flight.objects.all()
        return render(request, "admin/route_assign.html", {'flights': flights, 'routes': routes})

def view_route_assign(request):
    # Fetching tbl_routeassign objects along with related flight and route details
    assigns = tbl_routeassign.objects.select_related('flight', 'route').all()
    return render(request, "admin/view_route_assign.html", {'result': assigns})

def cancel_routeassign(request,id):
    detail = get_object_or_404(tbl_routeassign, id=id)
    detail.status = 'Cancelled'
    detail.save()
    return redirect(view_route_assign)

def view_bookings(request):

    bookings = tbl_bookingmaster.objects.all()
    for booking in bookings:
        # Count the number of passengers associated with the booking master ID
        passenger_count = tbl_bookingchild.objects.filter(bookingmaster_id=booking.id).count()
        
        # Convert total_traveller_no to integer for comparison
        total_traveller_no = int(booking.total_traveller_no)

        # Check if the passenger count matches the total_traveller_no
        booking.has_all_passengers = passenger_count == total_traveller_no
        
        # Check if the corresponding master ID exists in the tbl_payment table
        booking.has_payment = tbl_payment.objects.filter(bookingmaster_id=booking.id).exists()
        
        # Check if the flight status is 'Cancelled' in tbl_routeassign
        booking.flight_cancelled = tbl_routeassign.objects.filter(
            id=booking.routeassign.id,
            status='Cancelled'
        ).exists()

    return render(request, "admin/view_bookings.html", {'bookings': bookings})

def view_ticket_admin(request, id):
    booking = get_object_or_404(tbl_bookingmaster, id=id)
    passengers = tbl_bookingchild.objects.filter(bookingmaster=booking)
    
    return render(request, "admin/view_ticket.html", {'booking': booking, 'passengers': passengers})
#customer

def view_flights_user(request):
    current_date = date.today()
    assigns = tbl_routeassign.objects.select_related('flight', 'route').filter(status='Active', departure_date__gte=current_date)
    return render(request, "view_flights_user.html", {'result': assigns})

def search(request):
    if request.method == "POST":
        starting_point = request.POST.get('starting_point')
        destination = request.POST.get('destination')
        date = request.POST.get('date')
        
        # Convert the date string to a datetime object
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            date = None
        
        if starting_point and destination and date:
            # Filter flights based on the provided starting point, destination, and date
            assigns = tbl_routeassign.objects.select_related('flight', 'route').filter(
                Q(route__starting_point__icontains=starting_point) & 
                Q(route__destination__icontains=destination) | Q(route__stop__icontains=destination),
                departure_date=date,
                status='Active'
            )
            
            return render(request, 'view_flights_user.html', {'result': assigns})
        else:
            # If any of the required fields are missing, return a message
            message = "Please provide starting point, destination, and date for the search."
            return render(request, 'view_flights_user.html', {'message': message})
    else:
        # If the request method is not POST, render the page without any search results
        assigns = tbl_routeassign.objects.select_related('flight', 'route').filter(status='Active')
        return render(request, 'view_flights_user.html', {'result': assigns})

def bookflight(request,id):
    assigns = tbl_routeassign.objects.get(id=id)
    return render(request, "bookflight.html", {'result': assigns})

def add_booking(request, id):
    if request.method == "POST":
        cust_id = request.session['cuid']
        routeassign_id = id
        type_class = request.POST.get('type_class')
        adult_num = int(request.POST.get('adult_num'))  # Convert to integer
        infant_num = int(request.POST.get('infant_num'))  # Convert to integer

        # Fetching route assignment details
        route_assignment = tbl_routeassign.objects.get(pk=routeassign_id)

        if type_class == 'first':
            rate = route_assignment.first_class_rate
        elif type_class == 'business':
            rate = route_assignment.business_class_rate
        else:  # Assuming type_class is 'normal'
            rate = route_assignment.normal_class_rate
        

        total_amount = (int(rate) * adult_num) + (int(route_assignment.infant_rate) * infant_num)


        # Calculating total number of travelers
        total_traveller_no = adult_num + infant_num

        # Creating and saving the booking
        customer = customer_reg.objects.get(pk=cust_id)
        route_assign = tbl_routeassign.objects.get(pk=routeassign_id)
        booking = tbl_bookingmaster(customer=customer, routeassign=route_assign, total_traveller_no=total_traveller_no, total_amount=total_amount, status='Booked')
        booking.save()

        return redirect(my_booking)



def my_booking(request):
    customer_id = request.session.get('cuid')
    if customer_id:
        bookings = tbl_bookingmaster.objects.filter(customer_id=customer_id)
        for booking in bookings:
            # Count the number of passengers associated with the booking master ID
            passenger_count = tbl_bookingchild.objects.filter(bookingmaster_id=booking.id).count()
            
            # Convert total_traveller_no to integer for comparison
            total_traveller_no = int(booking.total_traveller_no)

            # Check if the passenger count matches the total_traveller_no
            booking.has_all_passengers = passenger_count == total_traveller_no
            
            # Check if the corresponding master ID exists in the tbl_payment table
            booking.has_payment = tbl_payment.objects.filter(bookingmaster_id=booking.id).exists()
            
            # Check if the flight status is 'Cancelled' in tbl_routeassign
            booking.flight_cancelled = tbl_routeassign.objects.filter(
                id=booking.routeassign.id,
                status='Cancelled'
            ).exists()

        return render(request, "my_bookings.html", {'bookings': bookings})
    else:
        # Handle case when customer_id is not found in the session
        # Redirect or render an appropriate response
        return HttpResponse("Customer ID not found in session.")

def cancel_booking(request, id):
    detail = get_object_or_404(tbl_bookingmaster, id=id)
    detail.status = 'Cancelled'
    detail.save()
    return render(request, "index.html", {'message': 'Your Request for cancel is success .Amount will be refunt to the bank account with in 24 hrs'})


def add_passengers(request, id):
    if request.method == "POST":
        bookingmaster_id = id
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        idproof_no = request.POST.get('idproof_no')

        # Retrieve the booking master instance
        booking_master = get_object_or_404(tbl_bookingmaster, pk=bookingmaster_id)

        # Count existing passengers for the booking master ID
        existing_passengers_count = tbl_bookingchild.objects.filter(bookingmaster_id=bookingmaster_id).count()

        # Get the total_traveller_no for the booking master and convert it to an integer
        total_traveller_no = int(booking_master.total_traveller_no)

        # Check if adding the new passenger will exceed the total_traveller_no
        if existing_passengers_count < total_traveller_no:
            # If not, create and save the new passenger
            passenger = tbl_bookingchild(bookingmaster=booking_master, fname=fname, lname=lname, gender=gender, idproof_no=idproof_no)
            passenger.save()
            return redirect(my_booking)
        else:
            # If yes, handle the error (for example, display a message or redirect to an error page)
            return render(request, "index.html", {'message': 'Maximum number of passengers reached for this booking'})

    else:
        booking_master = get_object_or_404(tbl_bookingmaster, id=id)
        return render(request, "add_passengers.html", {'booking_master': booking_master})


def booking_payment(request,id):
    if request.method == "POST":
        if tbl_payment.objects.filter(bookingmaster_id=id).exists():
            return HttpResponse("Payment record already exists for this booking.")
        bookingmaster = get_object_or_404(tbl_bookingmaster, id=id)
        payment_amt = request.POST.get('payment_amt')
        card_no = request.POST.get('card_no')
        card_name = request.POST.get('card_name')
        card_type = request.POST.get('card_type')
        cvv = request.POST.get('cvv')

        passenger = tbl_payment(bookingmaster=bookingmaster, payment_amt=payment_amt, card_no=card_no, card_name=card_name, card_type=card_type,cvv=cvv,status='Paid')
        passenger.save()
        return redirect(my_booking)
    else:
        assigns = tbl_bookingmaster.objects.get(id=id)
        return render(request, "booking_payment.html", {'result': assigns})
    


def view_ticket(request, id):
    booking = get_object_or_404(tbl_bookingmaster, id=id)
    passengers = tbl_bookingchild.objects.filter(bookingmaster=booking)
    
    return render(request, "view_ticket.html", {'booking': booking, 'passengers': passengers})