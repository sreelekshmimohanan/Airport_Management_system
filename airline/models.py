from django.db import models

class customer_reg(models.Model):
    fname=models.CharField(max_length=150)
    hname=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    street=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    pin=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class staff_reg(models.Model):
    name=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    hname=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    pin=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class tbl_login(models.Model):
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    user_type=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class tbl_flight(models.Model):
    flight_name=models.CharField(max_length=150)
    flight_model=models.CharField(max_length=150)
    flight_maxcap=models.CharField(max_length=150)
    business_cap=models.CharField(max_length=150)
    first_cap=models.CharField(max_length=150)
    economy_cap=models.CharField(max_length=150)
    year=models.CharField(max_length=150)
    status=models.CharField(max_length=150)


class tbl_route(models.Model):
    starting_point=models.CharField(max_length=150)
    destination=models.CharField(max_length=150)
    distance=models.CharField(max_length=150)
    stop=models.CharField(max_length=150)
 
class tbl_routeassign(models.Model):
    route = models.ForeignKey(tbl_route, on_delete=models.CASCADE)
    flight = models.ForeignKey(tbl_flight, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    first_class_rate = models.DecimalField(max_digits=10, decimal_places=2)
    business_class_rate = models.DecimalField(max_digits=10, decimal_places=2)
    normal_class_rate = models.DecimalField(max_digits=10, decimal_places=2)
    infant_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=150)

     
class tbl_bookingmaster(models.Model):
    customer = models.ForeignKey(customer_reg, on_delete=models.CASCADE)
    routeassign = models.ForeignKey(tbl_routeassign, on_delete=models.CASCADE)
    total_traveller_no=models.CharField(max_length=150)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=150)

    
class tbl_bookingchild(models.Model):
    bookingmaster = models.ForeignKey(tbl_bookingmaster, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    idproof_no = models.CharField(max_length=150)

    
class tbl_payment(models.Model):
    bookingmaster = models.ForeignKey(tbl_bookingmaster, on_delete=models.CASCADE)
    payment_amt = models.CharField(max_length=150)
    card_no = models.CharField(max_length=150)
    card_name = models.CharField(max_length=150)
    card_type = models.CharField(max_length=150)
    cvv = models.CharField(max_length=150)
    status = models.CharField(max_length=150)

class tbl_luggage(models.Model):
    bookingmaster = models.ForeignKey(tbl_bookingmaster, on_delete=models.CASCADE)
    num_baggage = models.IntegerField()
    total_weight = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=150, default='Added')

class tbl_weather(models.Model):
    location = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

class tbl_feedback(models.Model):
    bookingmaster = models.OneToOneField(tbl_bookingmaster, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 stars
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
