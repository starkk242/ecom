from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from orders import models
from rest_framework import permissions


import json
import razorpay


# Create your views here.
class CreatePaymentLink(APIView):

    def post(self,request):
        client = razorpay.Client(auth=("rzp_test_4zOsXxmjPqBFOZ", "8jUzFwb1iVjaHCPF5VdaDB3f"))
        amount = request.data["amount"]
        callback_url = request.data["callback_url"]
        address = request.data["address"]
        user = request.user

        order_init = models.Order.create(
            user = user,
            billing_address = address,
            shipping_address = address,
            order_total = amount
        )

        data = {
            "customer": {
            "name": user.first_name + " " + user.last_name,
            "email": user.email,
            "contact": user.phone_number
        },
            "type": "link",
            "view_less": 1,
            "amount": amount,
            "currency": "INR",
            "description": "Order From Health Mania",
            "receipt": order_init.id,
            "reminder_enable": True,
            "sms_notify": 1,
            "email_notify": 1,
            "expire_by": 1661883633,
            "callback_url": callback_url,
            "callback_method": "get"
        }
        val = client.invoice.create(data=data)
        print(val)
        return {
            "url":val['short_url']
                }
