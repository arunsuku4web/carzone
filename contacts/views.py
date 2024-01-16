from django.shortcuts import redirect, render
from django.contrib import messages

from contacts.models import Contact
#from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
      if request.method=='POST':

         car_id=request.POST['car_id']
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         customer_need=request.POST['customer_need']
         car_title=request.POST['car_title']
         city=request.POST['city']
         state=request.POST['state']
         email=request.POST['email']
         phone=request.POST['phone']
         message=request.POST['message']
         user_id=request.POST['user_id']

         if request.user.is_authenticated:
              user_id=request.user.id
              has_cotacted=Contact.objects.all().filter(user_id=user_id,car_id=car_id)
              if has_cotacted:
                   messages.error(request,'Your have already made an enquiry for this car, Please wait until we get back to you.')
                   return redirect('/cars/'+car_id)
              else:
                contact=Contact(car_id=car_id,first_name=first_name,
                         last_name=last_name,customer_need=customer_need,
                         car_title=car_title,city=city,state=state,
                         email=email,phone=phone,message=message,user_id=user_id
                         )
                admin_info=User.objects.get(is_superuser=True)
                admin_email=admin_info.email
               #  send_mail(
               #  "New Car Inquiry",
               #  "You have a new inquiry for the car ."+car_title+". Please login to your admin panel for more info.",
               #  "arunsuku4u@gmail.com",
               #  [admin_email],
               #  #fail_silently=False,
               #  )

                contact.save()
                messages.success(request,'Your request has been submitted, we will get back to you shortly.')

                return redirect('/cars/'+car_id)
