import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
import jdatetime

from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse

from .timeIR import *
from carts.cart import Cart
from .forms import RezervTeamForm, RezerOstadForm

from .helper_rezerv_ostad import send_request_to_rezerv_ostad_zarinapl
from .models import MyTeamModel, UserOstadModel, BokingDate,BokingDate_MyTeam

from .rezerv_helper import send_request_to_rezerv_zarinapl


# list all team
def MyTeamView(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    ostads = UserOstadModel.objects.all()
    teams = MyTeamModel.objects.all()
    return render(request, 'myteam/my_team.html', {'ostads': ostads, 'teams': teams, 'cart': cart})


# detail team
def UserDetailView(request, pk):
    rezerv = MyTeamModel()
    cart = Cart(request)
    user: MyTeamModel = get_object_or_404(MyTeamModel, pk=pk)

    return render(request, 'myteam/user_detail.html',
                  {'user': user,
                   'cart': cart,
                   'form': rezerv
                   })


# rezerv time team
def RezervTeamView(request, pk):
    user = get_object_or_404(MyTeamModel, pk=pk)
    if request.method == 'POST':
        rezerv = RezervTeamForm(request.POST)
        if rezerv.is_valid():
            rezerv_new = rezerv.save(commit=False)
            rezerv_new.user = user
            rezerv_new.save()
            try:
                redirect_url, authority = send_request_to_rezerv_zarinapl(request, rezerv_id=rezerv_new.id)
                rezerv_new.authority = authority
                rezerv_new.save()
                return redirect(redirect_url)
            except Exception as e:
                logging.error(e)
                response = HttpResponse("خطایی در سفارش پیش آمده است.")
                response.status_code = 406
                return response
        else:
            messages.warning(request, 'لطفا اطلاعات خرید را درست وارد کنید')
            return render(request, 'myteam/user_detail.html', {'user': user})


# detail leila-moammer
def OstadDetailView(request, pk):
    cart = Cart(request)
    user = get_object_or_404(UserOstadModel, pk=pk)
    return render(request, 'myteam/ostad_detail.html', {'ostads': user, 'cart': cart})


def RezervOstadView(request, pk):
    cart = Cart(request)
    ostad = get_object_or_404(UserOstadModel, pk=pk)
    if request.method == 'POST':
        response = RezerOstadForm(request.POST)
        if response.is_valid():
            res = response.save()
            try:
                redirect_url, authority = send_request_to_rezerv_ostad_zarinapl(request, rezerv_ostad_id=res.id)
                res.authority = authority
                response.save()
                return redirect(redirect_url)
            except Exception as e:
                logging.error(e)
                response = HttpResponse("خطایی در سفارش پیش آمده است.")
                response.status_code = 406
                return response
        else:
            messages.warning(request, 'لطفا اطلاعات خرید را درست وارد کنید')
            return render(request, 'myteam/ostad_detail.html', {'ostads': ostad, 'cart': cart})


@api_view(['POST'])
def checkmounth(request):
    
    mounthnow = int(ShowDateMonth())
    daynow = int(ShowDateDay())
    mounth = request.POST['mounth']
    id_team = request.POST['id_team']
    m1=[1,2,3,4,5,6]#نماینده 6 ماه اول سال که 31 روز است
    m2=[7,8,9,10,11]#نماینده 5 ماه از سال که 30 روز است
    employ = UserOstadModel.objects.get(id=id_team)
    a = []
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31]
    if int(mounth) in m1:
            pass
    elif int(mounth) in m2:
           r.pop()  
    else:
        r.pop()
        r.pop() 
    bookdate = BokingDate.objects.filter(employ=employ)
    # دریافت روزهای رزروی برای لیلا معمر
    
    for i in bookdate:
        
        if int(mounth) is i.date.month:
            a.append(i)
           
    # پیدا کردن روزهایی که تایم رزرو پر است        
    for j in a:
        if j.time1 and j.time2 and j.time3:
            rem = j.date.day - 1
            r.pop(rem)

    if mounthnow == int(mounth):
        r = r[daynow - 1:]
          
    
           
    return Response({'freeday': r})


@api_view(['POST'])
def checkrooztime(request):
    mounthnow = int(ShowDateMonth())
    daynow = int(ShowDateDay())
    rooz = request.POST['rooz']
    id_team = request.POST['id_team']

    employ = UserOstadModel.objects.get(id=id_team)
    a = []
    r = ["13:00", "14:00", "15:00"]
    rr = []
    bookdate = BokingDate.objects.filter(employ=employ)
    for i in bookdate:
        if int(rooz) is i.date.day:
            a.append(i)

    for j in a:
        if j.time1:
            rr.append("13:00")
        if j.time2:
            rr.append("14:00")
        if j.time3:
            rr.append("15:00")
    temp3 = []
    for element in r:
        if element not in rr:
            temp3.append(element)
    
    return Response({'freetime': temp3})


@api_view(['POST'])
def checkyear(request):
    mounthnow = int(ShowDateMonth())
    currentyear = int(ShowDateYear())
    year = request.POST['checkyear']
    
    year = int(year)
    mounthnow = int(mounthnow)
    r = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    if currentyear == year:
        r = r[mounthnow - 1:]
    else:
        pass
    
    return Response({'month': r})


@api_view(['POST'])
def reserv(request):
    daynow = int(ShowDateDay())
    mounthnow = int(ShowDateMonth())

    
    sal = request.POST['sallist']
    mounth = request.POST['mahlist']
    rooz = request.POST['roozlist']
    time = request.POST['timelist']
    name = request.POST['name']
    phone = request.POST['phone']
    service = request.POST['service']
    id_team = request.POST['id_team']
    employ = UserOstadModel.objects.get(id=id_team)
    date = jdatetime.date(int(sal), int(10), int(rooz))
    book = BokingDate.objects.filter(employ=employ, date=date)
    if book:
        if time == "13:00":
            book[0].time1 = True
            book[0].user1 = name
            book[0].phone1 = phone
            book[0].service1 = service
            book[0].save()
            print("New Update")

        elif time == "14:00":
            book[0].time2 = True
            book[0].user2 = name
            book[0].phone2 = phone
            book[0].service2 = service
            book[0].save()
            print("New Update")
        else:
            book[0].time3 = True
            book[0].user3 = name
            book[0].phone3 = phone
            book[0].service3 = service
            book[0].save()
            print("New Update")
    else:
        if time == "13:00":
            user1 = name
            phone1 = phone
            phone2 = None
            phone3 = None
            user2 = None
            user3 = None
            time1 = True
            time2 = False
            time3 = False
            service1 = service
            service2 = None
            service3 = None

        elif time == "14:00":
            user2 = name
            user1 = None
            user3 = None
            phone1 = None
            phone2 = None
            phone3 = phone
            time2 = True
            time3 = False
            time1 = False
            service1 = None
            service2 = service
            service3 = None
        else:
            user3 = name
            user2 = None
            user1 = None
            phone1 = None
            phone2 = phone
            phone3 = None
            time3 = True
            time2 = False
            time1 = False
            service1 = None
            service2 = None
            service3 = service
        BokingDate.objects.create(employ=employ, date=date, user1=user1, user2=user2, user3=user3, time1=time1,
                                  time2=time2, time3=time3, phone1=phone1,
                                  phone2=phone2, phone3=phone3, service1=service1, service2=service2,
                                  service3=service3).save()
        print("New Booking")

    return render(request, 'myteam/reserv.html', {'msg': 'رزرو شما با موفقیت ثبت شد'})


# Team View

@api_view(['POST'])
def checkmounth_team(request):
    
    mounthnow = int(ShowDateMonth())
    daynow = int(ShowDateDay())
    mounth = request.POST['mounth']
    id_team = request.POST['id_team']
    m1=[1,2,3,4,5,6]#نماینده 6 ماه اول سال که 31 روز است
    m2=[7,8,9,10,11]#نماینده 5 ماه از سال که 30 روز است
    employ = MyTeamModel.objects.get(id=id_team)
    a = []
    r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31]
    if int(mounth) in m1:
            pass
    elif int(mounth) in m2:
           r.pop()  
    else:
        r.pop()
        r.pop() 
    bookdate = BokingDate_MyTeam.objects.filter(employ=employ)
    # دریافت روزهای رزروی برای لیلا معمر
    
    for i in bookdate:
        
        if int(mounth) is i.date.month:
            a.append(i)
           
    # پیدا کردن روزهایی که تایم رزرو پر است        
    for j in a:
        if j.time1 and j.time2 and j.time3:
            rem = j.date.day - 1
            r.pop(rem)

    if mounthnow == int(mounth):
        r = r[daynow - 1:]
          
    
           
    return Response({'freeday': r})


@api_view(['POST'])
def checkrooztime_team(request):
    mounthnow = int(ShowDateMonth())
    daynow = int(ShowDateDay())
    rooz = request.POST['rooz']
    id_team = request.POST['id_team']
    employ = MyTeamModel.objects.get(id=id_team)
    a = []
    r = ["13:00", "14:00", "15:00"]
    rr = []
    bookdate = BokingDate_MyTeam.objects.filter(employ=employ)
    for i in bookdate:
        if int(rooz) is i.date.day:
            a.append(i)

    for j in a:
        if j.time1:
            rr.append("13:00")
        if j.time2:
            rr.append("14:00")
        if j.time3:
            rr.append("15:00")
    temp3 = []
    for element in r:
        if element not in rr:
            temp3.append(element)
    
    return Response({'freetime': temp3})


@api_view(['POST'])
def checkyear_team(request):
    mounthnow = int(ShowDateMonth())
    currentyear = int(ShowDateYear())
    year = request.POST['checkyear']
    year = int(year)
    mounthnow = int(mounthnow)
    r = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
    if currentyear == year:
        r = r[mounthnow - 1:]
    else:
        pass
    
    return Response({'month': r})


@api_view(['POST'])
def reserv_team(request):
    daynow = int(ShowDateDay())
    mounthnow = int(ShowDateMonth())
    id_team = request.POST['id_team']
    
    sal = request.POST['sallist']
    mounth = request.POST['mahlist']
    rooz = request.POST['roozlist']
    time = request.POST['timelist']
    name = request.POST['name']
    phone = request.POST['phone']
    service = request.POST['service']

    employ = MyTeamModel.objects.get(id=id_team)
    date = jdatetime.date(int(sal), int(10), int(rooz))
    book = BokingDate_MyTeam.objects.filter(employ=employ, date=date)
    if book:
        if time == "13:00":
            book[0].time1 = True
            book[0].user1 = name
            book[0].phone1 = phone
            book[0].service1 = service
            book[0].save()
            print("New Update")

        elif time == "14:00":
            book[0].time2 = True
            book[0].user2 = name
            book[0].phone2 = phone
            book[0].service2 = service
            book[0].save()
            print("New Update")
        else:
            book[0].time3 = True
            book[0].user3 = name
            book[0].phone3 = phone
            book[0].service3 = service
            book[0].save()
            print("New Update")
    else:
        if time == "13:00":
            user1 = name
            phone1 = phone
            phone2 = None
            phone3 = None
            user2 = None
            user3 = None
            time1 = True
            time2 = False
            time3 = False
            service1 = service
            service2 = None
            service3 = None

        elif time == "14:00":
            user2 = name
            user1 = None
            user3 = None
            phone1 = None
            phone2 = None
            phone3 = phone
            time2 = True
            time3 = False
            time1 = False
            service1 = None
            service2 = service
            service3 = None
        else:
            user3 = name
            user2 = None
            user1 = None
            phone1 = None
            phone2 = phone
            phone3 = None
            time3 = True
            time2 = False
            time1 = False
            service1 = None
            service2 = None
            service3 = service
        BokingDate_MyTeam.objects.create(employ=employ, date=date, user1=user1, user2=user2, user3=user3, time1=time1,
                                  time2=time2, time3=time3, phone1=phone1,
                                  phone2=phone2, phone3=phone3, service1=service1, service2=service2,
                                  service3=service3).save()
        print("New Booking")

    return render(request, 'myteam/reserv.html', {'msg': 'رزرو شما با موفقیت ثبت شد'})