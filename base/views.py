from json import JSONDecodeError
from django.shortcuts import render
from .models import Image

import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

def indexView(request):
    try:
        images = Image.objects.all()
        
        return render(request,'base/index.html',{
            'imagesFound' : True,
            'images' : images
        })
    except Exception as exc:
        return render(request, 'base/index.html', {
            'imagesFound' : False
        })


def imageById(request, imgId):
    image = Image.objects.get(id = imgId)

    return render(request,'base/image-detail.html', {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'imagesFound': True,
        'image': image,
    })

def SuccessView(request, imgId):
    image = Image.objects.get(id = imgId)
    return render(request,'base/success.html', {
        'image': image
    })

def CancelView(request):
    return render(request,'base/cancel.html')

def CreateCheckoutSessionView(request, imgId):
        
        image = Image.objects.get(id = imgId)
        imgPrice = image.price
        imgPrice = (imgPrice/80) *100
        imgPrice = int(imgPrice)

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': imgPrice,
                    'product_data': {
                        'name': image.image_type,
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success/' + str(image.id),
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
        return JsonResponse({
            'id': checkout_session.id
        }) 