"""airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index),
    path('cus_register',views.cus_register),

    path('login/',views.login),
    path('login/addlogin',views.addlogin),
    path('logout/',views.logout),

    path('dash',views.dash),

    path('staff_register/',views.staff_register),
    path('staff_register/add_staff_register',views.add_staff_register),
    path('view_staff',views.view_staff),
    path('removestaff/<int:id>',views.removestaff),

    path('view_cus',views.view_cus),
    path('removecustomer/<int:id>',views.removecustomer),

    path('add_flights',views.add_flights),
    path('view_flights',views.view_flights),

    path('edit_flight/<int:id>',views.edit_flight),
    path('edit_flight/edit_flight/<int:id>',views.edit_flight),
    path('remove_flight/<int:id>',views.remove_flight),

    path('add_route',views.add_route),
    path('view_route',views.view_route),
    path('route_assign',views.route_assign),
    path('view_route_assign',views.view_route_assign),
    path('cancel_routeassign/<int:id>',views.cancel_routeassign),

    path('view_flights_user',views.view_flights_user),
    path('bookflight/<int:id>',views.bookflight),
    path('bookflight/add_booking/<int:id>',views.add_booking),
    path('add_passengers/<int:id>',views.add_passengers),
    path('add_passengers/add_passengers/<int:id>',views.add_passengers),

    path('booking_payment/<int:id>',views.booking_payment),
    path('booking_payment/booking_payment/<int:id>',views.booking_payment),

    path('view_ticket/<int:id>',views.view_ticket),
    path('cancel_booking/<int:id>',views.cancel_booking),
    path('view_ticket_admin/<int:id>',views.view_ticket_admin),


    path('my_booking',views.my_booking),
    path('search',views.search),
    path('view_bookings',views.view_bookings),









    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
