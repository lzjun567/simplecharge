# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from charge.models import Charge
from django.db.models import Sum,Avg


def home(request):
    return render_to_response('index.html',{})
def index(request):

    username = request.GET.get('username')
    users = User.objects.all()
    charges = None
    print username
    if username:
        user = User.objects.get(username=username)
        charges = Charge.objects.filter(owner=user)

    return render_to_response('stat.html',{
        'users':users,
        'charges':charges,
    })

def stat(request):
    
    username = request.GET.get('username')
    users = User.objects.all()
    charges = None
    sum_amount=None
    avg_amount = None
    print username
    if username:
        user = User.objects.get(username=username)
        charges = Charge.objects.filter(owner=user)
        sum_amount = Charge.objects.filter(owner=user).aggregate(Sum('amount'))
        avg_amount  = Charge.objects.filter(owner=user).aggregate(Avg('amount'))
        print sum_amount
        print type(sum_amount)

    return render_to_response('data.html',{
        'users':users,
        'charges':charges,
        'sum_amount':sum_amount,
        'avg_amount':avg_amount,
    })
