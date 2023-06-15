from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
# Create your views here.


def Index(request):
    cl=MpesaClient()
    phone_number='0745904565'
    amount=1
    account_reference='CompanyXLTD'
    transaction_desc='Payment to daraja-sandbox'
    callback_url='https://darajambili.herokuapp.com/express-payment'
    response=cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
    return HttpResponse(response)
