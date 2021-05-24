from django.shortcuts import render
import razorpay
from .models import Coffe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

def home(request):
    if request.method =="POST":
        name= request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        email = request.POST.get("email")
        client = razorpay.Client(auth =("rzp_test_rD0wv59lvmLapP","ajYc8euRPGfd31WCxgmP8NZN"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        coffe = Coffe(name=name,amount=amount,email=email,payment_id = payment['id'],)
        coffe.save()
        return render(request,'index.html',{'payment':payment})
    return render(request,"index.html")


@csrf_exempt
def success(request):
    if request.method =='POST':
        a = request.POST
        order_id = ""
        for key , val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Coffe.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
    return render(request,"success.html")
