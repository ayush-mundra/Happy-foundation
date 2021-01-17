from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def pay(request):
    if request.method == "POST":
        amount = 50000
        order_currency = 'INR'
        

# client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     amount = 50000

    # client = razorpay.Client(auth=("rzp_live_4jh8hMv539N0rm", "RtVNts9SZLXkCW4yeJ8e2Yro"))

    client = razorpay.Client(
            auth=("rzp_live_4jh8hMv539N0rm", "RtVNts9SZLXkCW4yeJ8e2Yro"))

    payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")