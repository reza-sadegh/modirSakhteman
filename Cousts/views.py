from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Cousts,Categories
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    nowt=dt.datetime.today()
    extra_context = {'myname':'reza','rdate':nowt}
    
def all_cousts(request):
  #cousts = Cousts.objects.all().order_by('-payTime')
  #page_num = request.GET.get('page', 1)
  #paginator = Paginator(cousts, 3)
  #page_obj = paginator.page(page_num)
  #return render(request, 'all_cousts.html', {'page_obj': page_obj,'cnt':Cousts.objects.count,'sum':Cousts.objects.aggregate(Sum('Amount'))})
  #return redirect('/search_rep/?start_date=&end_date=&category=[ALL]&page=1')
  return redirect('/home/?start_date=&end_date=&category=[ALL]&page=1')

def search_min(request):
  categories = Categories.objects.all()
  return render(request,'search_min.html',{"categories":categories})
  
def search_rep(request):
  if (request.GET['start_date']): start_date = request.GET['start_date']
  else: start_date=dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date()

  if (request.GET['end_date']): end_date = request.GET['end_date']
  else: end_date=dt.datetime.strptime("2090-01-01", "%Y-%m-%d").date()

  if (request.GET['category']=='[ALL]'):
    cousts = Cousts.objects.filter(payTime__gte=start_date, payTime__lte=end_date).order_by('-payTime')
  else:
    category = request.GET['category']
    cousts = Cousts.objects.filter(payTime__gte=start_date, payTime__lte=end_date,category_name=category).order_by('-payTime')

  # cousts = Cousts.objects.all()
  page_num = request.GET.get('page', 1)
  paginator = Paginator(cousts, 3)
  page_obj = paginator.page(page_num)
  return render(request, 'search_rep.html',  {'page_obj': page_obj,'cnt':cousts.count,'sum':cousts.aggregate(Sum('Amount'))})

def add(request):
  categories = Categories.objects.all()
  return render(request,'add.html',{"categories":categories})

def addrecord(request):

  d = request.POST['description']
  a = request.POST['amount']
  r = request.POST['recipient']
  c = request.POST['categories']
  dt = request.POST['date']

  cousts = Cousts(Description=d, Amount=a,Recipient=r,category_name=c,payTime=dt)
  cousts.save()
  return HttpResponseRedirect(reverse('cousts'))

def delete(request, id):
  employee = Cousts.objects.get(id=id)
  employee.delete()
  return HttpResponseRedirect(reverse('cousts'))

def update(request, id):
  coust = Cousts.objects.get(id=id)
  categories = Categories.objects.all()
  template = loader.get_template('update.html')
  context = {
    'coust': coust,
    'categories':categories
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  d = request.POST['description']
  a = request.POST['amount']
  r = request.POST['recipient']
  c = request.POST['category']
  dt = request.POST['date']

  coust = Cousts.objects.get(id=id)

  coust.Description = d
  coust.Amount = a
  coust.Recipient = r
  coust.category_name = c
  coust.payTime = dt

  coust.save()

  return HttpResponseRedirect(reverse('cousts'))

@login_required(login_url='/accounts/login/')
def cousts(request):
  #cousts = Cousts.objects.all().order_by('-payTime')
  #page_num = request.GET.get('page', 1)
  #paginator = Paginator(cousts, 3)
  #page_obj = paginator.page(page_num)
  #return render(request, 'cousts.html', {'page_obj': page_obj})
  return redirect('/search_res/?description=&recipient=&minamount=&maxamount=&start_date=&end_date=&category=[ALL]&page=1')
  
@login_required(login_url='/accounts/login/')
def search_form(request):
  categories = Categories.objects.all()
  return render(request,'search_form.html',{"categories":categories})

def search_res(request):

  des=request.GET.get('description')
  res=request.GET.get('recipient')

  if(request.GET['minamount']):minamount=int(request.GET['minamount'])
  else:minamount=0

  if(request.GET['maxamount']):maxamount=int(request.GET['maxamount'])
  else:maxamount=10000000000

  if (request.GET['start_date']): start_date = request.GET['start_date']
  else: start_date=dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date()

  if (request.GET['end_date']): end_date = request.GET['end_date']
  else: end_date=dt.datetime.strptime("2090-01-01", "%Y-%m-%d").date()

  if (request.GET['category']=='[ALL]'):
    cousts = Cousts.objects.filter(Description__contains=des, Recipient__contains=res,Amount__gt=minamount, Amount__lt=maxamount,
                                         payTime__gte=start_date, payTime__lte=end_date).order_by('-payTime')
  else:
    category = request.GET['category']
    cousts = Cousts.objects.filter(Description__contains=des, Recipient__contains=res,Amount__gt=minamount, Amount__lt=maxamount,
                                         payTime__gte=start_date, payTime__lte=end_date,category_name=category).order_by('-payTime')

  page_num = request.GET.get('page', 1)
  paginator = Paginator(cousts, 3)
  page_obj = paginator.page(page_num)
  return render(request, 'search_res.html',  {'page_obj': page_obj,'cnt':cousts.count,'sum':cousts.aggregate(Sum('Amount'))})

def search_min_rep(request):

# if(request.method=='GET'):
  categories = Categories.objects.all()
  if ('start_date' in request.GET and request.GET['start_date']): start_date = request.GET['start_date']
  else: start_date = dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date()

  if ('end_date' in request.GET and request.GET['end_date']): end_date = request.GET['end_date']
  else: end_date=dt.datetime.strptime("2090-01-01", "%Y-%m-%d").date()

  if ('category'in request.GET ):category= request.GET['category']
  else:category='[ALL]'
  if (category=='[ALL]'):
    cousts = Cousts.objects.filter(payTime__gte=start_date, payTime__lte=end_date).order_by('-payTime').order_by('-payTime')
  else:
    cousts = Cousts.objects.filter(payTime__gte=start_date, payTime__lte=end_date,category_name=category).order_by('-payTime')
  page_num = request.GET.get('page', 1)
  paginator = Paginator(cousts,5)
  page_obj = paginator.page(page_num)

  return render(request, 'search_min_rep.html', {'page_obj': page_obj,'cnt':cousts.count,'sum':cousts.aggregate(Sum('Amount')),'categories':categories})










