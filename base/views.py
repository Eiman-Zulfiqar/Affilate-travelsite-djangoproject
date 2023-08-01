from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'plan.html')

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        textarea=request.POST.get('textarea')
    
        data=Contact(Name=name, Email=email, Phone_no=phone, Messege=textarea)
        data.save()

        # send_mail(
        #     subject='Inquiry Mail',
        #     message=f'Name: {name}\nEmail: {email}\nPhone#: {phone}\nMessage: {textarea}',
        #     from_email=email,  # Use the sender's email address as the "from_email"
        #     recipient_list=[settings.EMAIL_HOST_USER],  # Send the email to your email address
        #     fail_silently=False,
        # )
        return HttpResponse('Thankyou for contacting us!')
       

    return render(request, 'index.html', {})
    