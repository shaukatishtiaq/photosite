from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name= 'index'),
    path('image/<str:imgId>', views.imageById, name='image-detail'),
    path('create-checkout-session/<str:imgId>/', views.CreateCheckoutSessionView, name='create-checkout-session'),
    path('cancel/',views.CancelView, name='cancel'),
    path('success/<str:imgId>',views.SuccessView, name='success'),
]