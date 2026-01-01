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
from django.core.mail import send_mail

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
        fnames = request.POST.getlist('fname')
        lnames = request.POST.getlist('lname')
        genders = request.POST.getlist('gender')
        idproof_nos = request.POST.getlist('idproof_no')

        # Retrieve the booking master instance
        booking_master = get_object_or_404(tbl_bookingmaster, pk=bookingmaster_id)

        # Count existing passengers for the booking master ID
        existing_passengers_count = tbl_bookingchild.objects.filter(bookingmaster_id=bookingmaster_id).count()

        # Get the total_traveller_no for the booking master and convert it to an integer
        total_traveller_no = int(booking_master.total_traveller_no)

        # Loop through the submitted passengers
        added_count = 0
        for i in range(len(fnames)):
            if existing_passengers_count + added_count < total_traveller_no:
                passenger = tbl_bookingchild(bookingmaster=booking_master, fname=fnames[i], lname=lnames[i], gender=genders[i], idproof_no=idproof_nos[i])
                passenger.save()
                added_count += 1
            else:
                break

        return redirect(my_booking)

    else:
        booking_master = get_object_or_404(tbl_bookingmaster, id=id)
        existing_passengers_count = tbl_bookingchild.objects.filter(bookingmaster_id=id).count()
        total_traveller_no = int(booking_master.total_traveller_no)
        remaining = total_traveller_no - existing_passengers_count
        remaining_list = list(range(remaining))
        return render(request, "add_passengers.html", {'booking_master': booking_master, 'remaining_list': remaining_list})


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

        # Send email notification
        customer_email = bookingmaster.customer.email
        subject = 'Booking Confirmation'
        passengers = tbl_bookingchild.objects.filter(bookingmaster=bookingmaster)
        passenger_details = '\n'.join([f"{p.fname} {p.lname}, Gender: {p.gender}, ID: {p.idproof_no}" for p in passengers])
        message = f"""
Dear {bookingmaster.customer.fname},

Your booking has been confirmed and payment processed successfully.

Booking Details:
- Booking ID: {bookingmaster.id}
- Route: {bookingmaster.routeassign.route.starting_point} to {bookingmaster.routeassign.route.destination}
- Flight: {bookingmaster.routeassign.flight.flight_name}
- Departure Date: {bookingmaster.routeassign.departure_date}
- Departure Time: {bookingmaster.routeassign.departure_time}
- Total Amount Paid: {payment_amt}

Passengers:
{passenger_details}

Thank you for choosing our service.

Best regards,
Airport Management System
"""
        send_mail(subject, message, 'sample@example.com', [customer_email])#replace with your EMAIL_HOST_USER

        return redirect(my_booking)
    else:
        assigns = tbl_bookingmaster.objects.get(id=id)
        return render(request, "booking_payment.html", {'result': assigns})
    


def view_ticket(request, id):
    booking = get_object_or_404(tbl_bookingmaster, id=id)
    passengers = tbl_bookingchild.objects.filter(bookingmaster=booking)
    
    return render(request, "view_ticket.html", {'booking': booking, 'passengers': passengers})

def add_luggage(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        num_baggage = request.POST.get('num_baggage')
        total_weight = request.POST.get('total_weight')
        description = request.POST.get('description')
        try:
            booking = tbl_bookingmaster.objects.get(id=booking_id)
            # Check if payment is completed
            if not tbl_payment.objects.filter(bookingmaster=booking, status='Paid').exists():
                return render(request, "admin/add_luggage.html", {'error': 'Payment not completed for this booking.'})
            luggage = tbl_luggage(bookingmaster=booking, num_baggage=num_baggage, total_weight=total_weight, description=description)
            luggage.save()
            # Update booking status to 'Boarded'
            booking.status = 'Boarded'
            booking.save()
            return render(request, "admin/index.html", {'message': 'Luggage details added successfully and booking status updated to Boarded'})
        except tbl_bookingmaster.DoesNotExist:
            return render(request, "admin/add_luggage.html", {'error': 'Invalid Booking ID'})
    else:
        return render(request, "admin/add_luggage.html")

def manage_luggage(request):
    if request.method == "POST":
        luggage_id = request.POST.get('luggage_id')
        new_status = request.POST.get('status')
        try:
            luggage = tbl_luggage.objects.get(id=luggage_id)
            luggage.status = new_status
            luggage.save()
            # If luggage status is 'Out for Pick Up', update booking status to 'Journey Completed'
            if new_status == 'Out for Pick Up':
                luggage.bookingmaster.status = 'Journey Completed'
                luggage.bookingmaster.save()
        except tbl_luggage.DoesNotExist:
            pass
    luggages = tbl_luggage.objects.select_related('bookingmaster').all()
    return render(request, "admin/manage_luggage.html", {'luggages': luggages})

def track_luggage(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        customer_id = request.session.get('cuid')
        if customer_id:
            try:
                booking = tbl_bookingmaster.objects.get(id=booking_id, customer_id=customer_id)
                luggage = tbl_luggage.objects.filter(bookingmaster=booking).first()
                if luggage:
                    return render(request, "track_luggage.html", {'luggage': luggage, 'booking': booking})
                else:
                    return render(request, "track_luggage.html", {'error': 'No luggage found for this booking.'})
            except tbl_bookingmaster.DoesNotExist:
                return render(request, "track_luggage.html", {'error': 'Invalid Booking ID or booking does not belong to you.'})
        else:
            return redirect('login')
    else:
        return render(request, "track_luggage.html")

def manage_weather(request):
    if request.method == "POST":
        location = request.POST.get('location')
        condition = request.POST.get('condition')
        temperature = request.POST.get('temperature')
        weather, created = tbl_weather.objects.get_or_create(location=location, defaults={'condition': condition, 'temperature': temperature})
        if not created:
            weather.condition = condition
            weather.temperature = temperature
            weather.save()
    # Get unique locations from routes
    locations = set()
    routes = tbl_route.objects.all()
    for route in routes:
        locations.add(route.starting_point)
        locations.add(route.destination)
    locations = sorted(list(locations))
    weathers = {w.location: w for w in tbl_weather.objects.filter(location__in=locations)}
    location_weather = [(loc, weathers.get(loc)) for loc in locations]
    return render(request, "admin/manage_weather.html", {'location_weather': location_weather})

def view_booking_weather(request, id):
    customer_id = request.session.get('cuid')
    if not customer_id:
        return redirect('login')
    try:
        booking = tbl_bookingmaster.objects.get(id=id, customer_id=customer_id)
    except tbl_bookingmaster.DoesNotExist:
        return render(request, "index.html", {'message': 'Booking not found.'})
    starting_point = booking.routeassign.route.starting_point
    destination = booking.routeassign.route.destination
    start_weather = tbl_weather.objects.filter(location=starting_point).first()
    dest_weather = tbl_weather.objects.filter(location=destination).first()
    return render(request, "view_booking_weather.html", {
        'booking': booking,
        'start_weather': start_weather,
        'dest_weather': dest_weather
    })

def give_feedback(request, id):
    customer_id = request.session.get('cuid')
    if not customer_id:
        return redirect('login')
    try:
        booking = tbl_bookingmaster.objects.get(id=id, customer_id=customer_id, status='Journey Completed')
    except tbl_bookingmaster.DoesNotExist:
        return render(request, "index.html", {'message': 'Feedback not available for this booking.'})
    
    if request.method == "POST":
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        feedback, created = tbl_feedback.objects.get_or_create(
            bookingmaster=booking,
            defaults={'rating': rating, 'comments': comments}
        )
        if not created:
            feedback.rating = rating
            feedback.comments = comments
            feedback.save()
        return redirect('my_booking')
    else:
        existing_feedback = tbl_feedback.objects.filter(bookingmaster=booking).first()
        return render(request, "give_feedback.html", {'booking': booking, 'feedback': existing_feedback})

def view_feedbacks(request):
    feedbacks = tbl_feedback.objects.select_related('bookingmaster__customer', 'bookingmaster__routeassign__route').all()
    return render(request, "admin/view_feedbacks.html", {'feedbacks': feedbacks})