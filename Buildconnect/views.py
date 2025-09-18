import datetime
import random
import smtplib
import razorpay
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from Buildconnect.models import *

projectemail = "buildconnect007@gmail.com"
projectpassword = "jkkn utcc oiue grds"


def index(request):
    return render(request, "index.html")



def Login(request):
    return render(request,'login.html')

def login_post(request):
    username1 = request.POST['textfield']
    password1 = request.POST['textfield2']

    request.session['login'] = '1'

    lobj = login.objects.filter(username = username1,password=password1)
    if lobj.exists():
        lobj = lobj[0]
        request.session['heading'] = ""
        if lobj.usertype == 'admin':
            return HttpResponse("<script>alert('login successfull');window.location='/home_page'</script>")
        elif lobj.usertype == 'user':
            request.session['lid']=lobj.id
            request.session['uid']=user.objects.get(LOGIN=lobj.id).id
            return HttpResponse("<script>alert('login successfull');window.location='/user_home'</script>")

        elif lobj.usertype == 'worker':
            request.session['lid'] = lobj.id
            request.session['wid'] = worker.objects.get(LOGIN=request.session['lid']).id
            print("worker_id", request.session['wid'])
            return HttpResponse("<script>alert('login successfull');window.location='/workerlink'</script>")

        else:
            return HttpResponse("<script>alert('Access denied');window.location='/'</script>")



    else:
        return HttpResponse("<script>alert('invalid');window.location='/'</script>")



#
# def loginS(request):
#     return render(request, "worker/login.html")

# def loginbuttonclick(request):
#     username = request.POST['textfield']
#     password = request.POST['textfield2']
#
#     request.session['login'] = '1'
#
#     lobj = login.objects.filter(username=username, password=password)
#     if lobj.exists():
#         lobj = lobj[0]
#         if lobj.usertype == 'admin':
#             return HttpResponse("<script>alert('login successfull');window.location='/home_page'</script>")
#
#
#         else:
#             return HttpResponse("<script>alert('invalid');window.location='/'</script>")
#     else:
#         return HttpResponse("<script>alert('invalid');window.location='/'</script>")





def view_workers_approve(request):
    request.session['heading'] = "New Workers"

    data = worker.objects.filter(LOGIN__usertype = 'pending')
    return render(request,'admin/view workers approve.html',{'data':data})

def view_approved_workers(request):
    request.session['heading'] = "Approved Workers"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = worker.objects.filter(LOGIN__usertype__in=['worker','block'])
    return render(request,'admin/view  approved workers.html',{'data':data})

def view_rejected_workers(request):
    request.session['heading'] = "Rejected Workers"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = worker.objects.filter(LOGIN__usertype='rejected')
    return render(request,'admin/view  rejected workers.html',{'data':data})

def view_workers_portfolio(request):
    request.session['heading'] = "Users"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = user.objects.filter()
    return render(request, 'admin/users.html', {'data':data})



def worker_portfolio(request,id):
    request.session['heading'] = "Workers Portfolio"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view1=portfolio.objects.filter(WORKER=id)
    return render(request, 'admin/view_portfolio.html', {'data': view1})



def view_Complaint(request):
    request.session['heading'] = "Complaint"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = complaint.objects.all()
    return render(request,'admin/view  Complaint.html',{'data':data})





def View_feed_back(request):
    request.session['heading'] = "Feedbacks"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = feedback.objects.all()
    return render(request,'admin/View feed back.html',{'data':data})


def home_page(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return  render(request,'admin/index.html')

def logout(request):
    request.session['login'] = '0'
    return HttpResponse("<script>alert('logout successfully');window.location='/'</script>")

def block(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="block")
    request.session['email'] =  login.objects.filter(id=id)[0].username
    return HttpResponse("<script>alert('blocked');window.location='/reason'</script>")
def unblock(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="worker")
    return HttpResponse("<script>alert('unblocked');window.location='/view_approved_workers'</script>")

def reason(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,'admin/reason.html')

def reason_submit(request):
    r = request.POST['textarea']
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(projectemail,projectpassword)
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = projectemail
    msg['To'] = request.session['email']
    msg['Subject'] = "Your Password for Smart Donation Website"
    body =r
    msg.attach(MIMEText(body,'plain'))
    s.send_message(msg)

    return HttpResponse("<script>alert('submitted');window.location='/view_approved_workers'</script>")

def wapprove(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="worker")
    # request.session['email'] =  login.objects.filter(id=id)[0].username
    # import smtplib
    # s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    # s.starttls()
    # s.login(projectemail,projectpassword)
    # msg = MIMEMultipart()  # create a message.........."
    # msg['From'] = projectemail
    # msg['To'] = request.session['email']
    # msg['Subject'] = "Your Password for Smart Donation Website"
    # body = 'your account is verified sucessfully'
    # msg.attach(MIMEText(body, 'plain'))
    # s.send_message(msg)
    return HttpResponse("<script>alert('approved');window.location='/view_approved_workers'</script>")

def wreject(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    login.objects.filter(id=id).update(usertype="rejected")
    request.session['email'] =  login.objects.filter(id=id)[0].username
    return HttpResponse("<script>alert('rejected');window.location='/reason'</script>")

#--------------------------------User---------------

def user_register(request):
    return render(request,"user/register.html")



def user_register_post(request):

    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    phone_number = request.POST['phone']
    gender = request.POST['gender']
    pincode = request.POST['pin']
    post_office = request.POST['post']
    place = request.POST['place']
    latitude = request.POST['lati']
    longitude = request.POST['longi']
    passw = request.POST['passw']
    cpassw = request.POST['cpassw']
    if passw == cpassw:


        obj1=login()
        obj1.username=email
        obj1.password=passw
        obj1.usertype="user"
        obj1.save()


        obj=user()
        obj.name=name
        obj.email=email
        obj.age=age
        obj.phone_number=phone_number
        obj.gender=gender
        obj.pincode=pincode
        obj.post_office=post_office
        obj.place=place
        obj.latitude=latitude
        obj.longitude=longitude
        obj.LOGIN_id=obj1.id
        obj.save()
        return HttpResponse("<script>alert('registered');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('please wait');window.location='/user_register'</script>")













def user_home(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,"user/home.html")

def user_view_and_edit_profile(request):
    request.session['heading'] = "User Profile"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=user.objects.get(LOGIN=request.session['lid'])
    return render(request,"user/view and edit profile.html",{"data":view})

def user_update(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    name = request.POST['name']
    age = request.POST['age']
    phone_number = request.POST['phone']
    gender = request.POST['gender']
    pincode = request.POST['pin']
    post_office = request.POST['post']
    place = request.POST['place']
    latitude = request.POST['lati']
    longitude = request.POST['longi']
    user.objects.filter(id=id).update(name=name,age=age,phone_number=phone_number,gender=gender,pincode=pincode,post_office=post_office,place=place,latitude=latitude,longitude=longitude)
    return HttpResponse("<script>alert('Updated');window.location='/user_view_and_edit_profile'</script>")

def user_view_workers(request):
    request.session['heading'] = "Workers"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=worker.objects.filter(LOGIN__usertype="worker")
    return render(request,"user/view workers.html",{"data":view})

def user_view_rating(request,id):
    request.session['heading'] = "Review and Rating"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=review.objects.filter(WORKER=id)
    return render(request,"user/view rating.html",{"data":view})

def user_view_workers_portfolio(request,id):
    request.session['heading'] = "Workers Portfolio"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=portfolio.objects.filter(WORKER=id)
    return render(request,"user/view workers portfolio.html",{"data":view})

def user_add_project_request(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,"user/add project request.html",{"id":id})
def request_send_post(request,id):
    request1 = request.POST['request']


    if requests.objects.filter(USER_id = request.session['uid'],PORTFOLIO_id = id,status='pending').exists():
        return HttpResponse(
            "<script>alert('Already exists');window.location='/user_view_workers#abc'</script>")

    obj = requests()
    obj.request = request1
    obj.request_date = datetime.datetime.now()
    obj.USER_id = request.session['uid']
    obj.PORTFOLIO_id = id
    obj.status="pending"
    obj.save()
    return HttpResponse("<script>alert('send');window.location='/user_view_workers#abc'</script>")


def user_view_project_request_status(request):
    request.session['heading'] = "Request Status"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=requests.objects.filter(USER=request.session['uid'])
    a=[]
    for i in view:
        view2=budget.objects.filter(REQUEST_id=i.id)

        if view2.exists():
            j = view2[0]
            p = payment.objects.filter(REQUEST=i.id)
            if p.exists():

                if len(p) == 2:
                    ad = float(j.price) - float(p[0].amount)
                    a.append({"id": i.id,
                              "request": i.request,
                              "request_date": i.request_date,
                              "status": i.status,
                              "PORTFOLIO": i.PORTFOLIO,
                              "name": i.PORTFOLIO.WORKER.name,
                              "age": i.PORTFOLIO.WORKER.age,
                              "email": i.PORTFOLIO.WORKER.email,
                              "gender": i.PORTFOLIO.WORKER.gender,
                              "phone_number": i.PORTFOLIO.WORKER.phone_number,
                              "pincode": i.PORTFOLIO.WORKER.pincode,
                              "post_office": i.PORTFOLIO.WORKER.post_office,
                              "place": i.PORTFOLIO.WORKER.place,
                              "price": j.price,
                              "bid": j.id,
                              "pay": "Payment completed",
                              "pay_status": "Payment completed"
                              })
                if len(p) == 1:

                    ad = float(int(j.price)) - float((p[0].amount))
                    a.append({"id": i.id,
                              "request": i.request,
                              "request_date": i.request_date,
                              "status": i.status,
                              "PORTFOLIO": i.PORTFOLIO,
                              "name": i.PORTFOLIO.WORKER.name,
                              "age": i.PORTFOLIO.WORKER.age,
                              "email": i.PORTFOLIO.WORKER.email,
                              "gender": i.PORTFOLIO.WORKER.gender,
                              "phone_number": i.PORTFOLIO.WORKER.phone_number,
                              "pincode": i.PORTFOLIO.WORKER.pincode,
                              "post_office": i.PORTFOLIO.WORKER.post_office,
                              "place": i.PORTFOLIO.WORKER.place,
                              "price": j.price,
                              "bid": j.id,
                              "pay": ad,
                              "pay_status": "Final"

                              })



            else:
                ad = int(j.price)/3
                a.append({"id": i.id,
                          "request": i.request,
                          "request_date": i.request_date,
                          "status": i.status,
                          "PORTFOLIO": i.PORTFOLIO,
                          "name": i.PORTFOLIO.WORKER.name,
                          "age": i.PORTFOLIO.WORKER.age,
                          "email": i.PORTFOLIO.WORKER.email,
                          "gender": i.PORTFOLIO.WORKER.gender,
                          "phone_number": i.PORTFOLIO.WORKER.phone_number,
                          "pincode": i.PORTFOLIO.WORKER.pincode,
                          "post_office": i.PORTFOLIO.WORKER.post_office,
                          "place": i.PORTFOLIO.WORKER.place,
                          "price": j.price,
                          "bid": j.id,
                          "pay": ad,
                          "pay_status": "Ad"

                          })

        else:
            a.append({"id": i.id,
                      "request": i.request,
                      "request_date": i.request_date,
                      "status": i.status,
                      "PORTFOLIO": i.PORTFOLIO,
                      "name": i.PORTFOLIO.WORKER.name,
                      "age": i.PORTFOLIO.WORKER.age,
                      "email": i.PORTFOLIO.WORKER.email,
                      "gender": i.PORTFOLIO.WORKER.gender,
                      "phone_number": i.PORTFOLIO.WORKER.phone_number,
                      "pincode": i.PORTFOLIO.WORKER.pincode,
                      "post_office": i.PORTFOLIO.WORKER.post_office,
                      "place": i.PORTFOLIO.WORKER.place,
                      "price": "No updates",
                      "bid":"0",
                      "pay_status": "No updates"

                      })

    return render(request,"user/view project request status.html",{"view":a})


def user_approve_budget(request,id,bid):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    requests.objects.filter(id=id).update(status="Finalized")
    budget.objects.filter(id=bid).update(status="approve")
    return HttpResponse("<script>alert('approved');window.location='/user_view_project_request_status#abc'</script>")

def user_reject_budget(request,id,bid):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    budget.objects.filter(id=bid).update(status="reject")
    return HttpResponse("<script>alert('rejected');window.location='/user_view_project_request_status#abc'</script>")

def user_view_materials(request,id):
    request.session['heading'] = "Materials"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=material.objects.filter(REQUEST=id)
    return render(request,"user/view material.html",{"data":view})

def user_send_rating_to_worker(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,"user/send rating to worker.html",{"id":id})

def user_send_feedback(request):
    request.session['heading'] = "User Feedback"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,"user/send feedback.html")

def send_feedbackbutton(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    complaint=request.POST['textarea']
    obj=feedback()
    obj.feedback=complaint
    obj.LOGIN_id = request.session['lid']
    obj.date = datetime.datetime.now().date()
    obj.save()
    return HttpResponse("<script>alert('Send sucessfull');window.location='/user_home'</script>")


def user_send_rating_to_worker_post(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    r = request.POST['star']
    re = request.POST['re']
    obj = review()
    obj.review = re
    obj.rating=r
    obj.review_date = datetime.datetime.now()
    obj.USER_id = request.session['uid']
    obj.WORKER_id = id
    obj.save()
    return HttpResponse("<script>alert('send review');window.location='/user_view_project_request_status#abc'</script>")


def user_send_complaint(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request,"user/send complaint.html",{"id":id})

def user_send_complaint_POST(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    complaint1 = request.POST['c']
    obj = complaint()
    obj.complaint = complaint1
    obj.complaint_date = datetime.datetime.now()
    obj.USER_id = request.session['uid']
    obj.WORKER_id = id
    obj.reply="pending"
    obj.reply_date = "pending"
    obj.save()

    return HttpResponse("<script>alert('complaint successfull');window.location='/user_home'</script>")

def user_view_reply(request):
    request.session['heading'] = "Complaint reply"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view=complaint.objects.filter(USER=request.session['uid'])
    return render(request,"user/view reply.html",{"data":view})

def user_change_password_GET(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "user/change password.html")

def user_change_password_POST(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    oldpassword = request.POST['old']
    newpassword = request.POST['new']
    confirmpassword = request.POST['confirm']

    if oldpassword == newpassword:
        return HttpResponse(
            "<script>alert('Pleae enter a new password');window.location='/user_change_password_GET'</script>")

    data=login.objects.filter(password=oldpassword,id= request.session['lid'],usertype="user")
    if data.exists():
        if newpassword == confirmpassword:
            login.objects.filter(id= request.session['lid']).update(password=confirmpassword)
            return HttpResponse("<script>alert('password changed');window.location='/user_home#abc'</script>")
        else:
            return HttpResponse(
                "<script>alert('password missmatch');window.location='/user_change_password_GET'</script>")
    else:
        return HttpResponse(
            "<script>alert('not found');window.location='/user_change_password_GET'</script>")




#-----------------------------------------------------------------------------


def payment_method(request,amount,id,m):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    request.session['m'] = m
    return render(request, "user/payment mode.html",{"id":id,"amount":amount})

def payment_post(request,amount,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    type=request.POST['radio']
    request.session['amount'] = amount
    request.session['rid'] = id
    if type == "offline":
        return redirect("/offline/"+id)
    else:
        return redirect("/default/"+id)


def offline(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    obj = payment()
    obj.REQUEST_id=id
    obj.payment_mode = "offline"
    obj.payment_date = datetime.datetime.now()
    obj.payment_status = request.session['m']
    obj.amount = request.session['amount']
    obj.save()
    return HttpResponse("<script>alert('payed suucessfully');window.location='/user_view_project_request_status#abc'</script>")


def default(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200*100
    amount=round(float(request.session['amount']),2)*100
    print(amount,"oooo")
    # amount = float(amount)

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    return render(request, 'user/payment.html',{'razorpay_api_key': razorpay_api_key,
                                            'amount': order_data['amount'],
                                            'currency': order_data['currency'],
                                            'order_id': order['id']})

def online(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    obj = payment()
    obj.REQUEST_id = request.session['rid']
    obj.payment_mode = "online"
    obj.payment_date = datetime.datetime.now()
    obj.payment_status = request.session['m']
    obj.amount = request.session['amount']
    obj.save()
    return HttpResponse(
        "<script>alert('payed suucessfully');window.location='/user_view_project_request_status#abc'</script>")


#-----------------------------------------------------------------------



    #########user_chat######

def chatt1(request,id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    request.session['wid'] = id
    return render(request, 'user/chat.html',{"id":id})

def chatsnd1(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    c = request.session['lid']
    m = request.POST['msg']
    cc = user.objects.get(LOGIN__id=c)
    uu = worker.objects.get(id=request.session['wid'])
    obj = chat()
    obj.message_date = d
    obj.message_send = 'user'
    obj.WORKER = uu
    obj.USER = cc
    obj.message_reply = m
    obj.save()
    print(obj)
    v = {}
    if int(obj.id) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse(v)
    return r

def chatrply1(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    c = request.session['lid']
    cc=user.objects.get(LOGIN__id=c)
    res = chat.objects.filter(WORKER=request.session['wid'], USER=cc)
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type': i.message_send,
                'message': i.message_reply,
                'name': 'Me',
                'id':i.USER.id,
                'upic':'/static/a.webp',
                'dtime': i.message_date,
                'tname': i.USER.name,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v})
    else:
        return JsonResponse({"status": "error"})


def register(request):
    return render(request, "worker/register.html")

def registerbuttonclick(request):
    Name = request.POST['name']
    Age = request.POST['age']
    Phoneno = request.POST['phone']
    Email = request.POST['email']
    Gender = request.POST['gender']
    Pincode = request.POST['pin']
    Postoffice = request.POST['post']
    Place = request.POST['place']
    Latidude = request.POST['lati']
    Longitude = request.POST['long']
    Password = request.POST['pass']
    Confirmpassword = request.POST['cpass']
    Skills = request.POST['s']
    Qualification = request.POST['q']

    if Password == Confirmpassword:
        obj = login()
        obj.username = Email
        obj.password = Password
        obj.usertype = 'pending'
        obj.save()

        obj1 = worker()
        obj1.name = Name
        obj1.age = Age
        obj1.phone_number = Phoneno
        obj1.email = Email
        obj1.gender = Gender
        obj1.pincode = Pincode
        obj1.post_office = Postoffice
        obj1.place = Place
        obj1.latitude = Latidude
        obj1.longitude = Longitude
        obj1.skills = Skills
        obj1.qualification = Qualification
        obj1.LOGIN_id = obj.id
        obj1.save()

        return HttpResponse("<script>alert('Registered successfully');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Incorrect password');window.location='/'</script>")

def view_and_edit_profile(request):
    request.session['heading'] = "Worker Profile"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = worker.objects.get(id=request.session['wid'])
    return render(request, "worker/view and edit profile.html", {'data': data})

def view_and_edit_profilebuttonclick(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Name = request.POST['textfield']
    Age = request.POST['textfield2']
    Phoneno = request.POST['textfield3']
    Email = request.POST['textfield4']
    Gender = request.POST['textfield5']
    Pincode = request.POST['textfield6']
    Postoffice = request.POST['textfield7']
    Place = request.POST['textfield8']
    Latidude = request.POST['textfield9']
    Longitude = request.POST['textfield10']
    s = request.POST['s']
    q = request.POST['q']

    worker.objects.filter(id=request.session['wid']).update(name=Name, age=Age, phone_number=Phoneno, email=Email,
                                                            gender=Gender, pincode=Pincode, post_office=Postoffice,
                                                            place=Place, latitude=Latidude, longitude=Longitude,skills=s,qualification=q)

    return HttpResponse("<script>alert('Updated');window.location='/view_and_edit_profile#home'</script>")

def add_portfolio(request):
    request.session['heading'] = "Add Portfolio"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/add portfolio.html")

def add_portfoliobuttonclick(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Image1 = request.FILES['fileField']
    Image2 = request.FILES['fileField2']
    Image3 = request.FILES['fileField3']
    Image4 = request.FILES['fileField4']
    Type = request.POST['select']
    Experience = request.POST['textarea']

    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs.save(r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d + '1.jpg',
            Image1)
    path1 = '/static/' + d + '1.jpg'
    d2 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d2 + '2.jpg',
            Image2)
    path2 = '/static/' + d2 + '2.jpg'

    d3 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d3 + '3.jpg',
            Image3)
    path3 = '/static/' + d3 + '3.jpg'

    d4 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d4 + '4.jpg',
            Image4)
    path4 = '/static/' + d4 + '4.jpg'

    obj1 = portfolio()
    obj1.image1 = path1
    obj1.image2 = path2
    obj1.image3 = path3
    obj1.image4 = path4
    obj1.type = Type
    obj1.experience = Experience
    obj1.WORKER_id = request.session['wid']
    obj1.save()
    return HttpResponse("<script>alert('Added');window.location='/view_portfolio#home'</script>")

def edit_portfolio(request):
    request.session['heading'] = "Update Portfolio"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/edit portfolio.html")

def edit_portfoliobuttonclick(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Type = request.POST['select']
    Experience = request.POST['textarea']

    if "fileField" in request.FILES:
        Image1 = request.FILES['fileField']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs.save(
            r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d + '1.jpg',
            Image1)
        path1 = '/static/' + d + '1.jpg'

        portfolio.objects.filter(id=id).update(image1=path1)

    if "fileField2" in request.FILES:
        Image2 = request.FILES['fileField2']
        fs = FileSystemStorage()
        d2 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs.save(
            r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d2 + '2.jpg',
            Image2)
        path2 = '/static/' + d2 + '2.jpg'
        #
        portfolio.objects.filter(id=id).update(image2=path2)

    if "fileField3" in request.FILES:
        Image3 = request.FILES['fileField3']
        d3 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs = FileSystemStorage()
        fs.save(
            r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d3 + '3.jpg',
            Image3)
        path3 = '/static/' + d3 + '3.jpg'
        portfolio.objects.filter(id=id).update(image3=path3)

    if "fileField4" in request.FILES:
        Image4 = request.FILES['fileField4']
        fs = FileSystemStorage()
        d4 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs.save(
            r"C:\Users\abhie\Downloads\newwww\Buidconnectnew\Buildconnect\static\\" + d4 + '4.jpg',
            Image4)
        path4 = '/static/' + d4 + '4.jpg'
        portfolio.objects.filter(id=id).update(image4=path4)

    portfolio.objects.filter(id=id).update(type=Type, experience=Experience)

    return HttpResponse("<script>alert('Updated');window.location='/view_portfolio#home'</script>")

def view_portfolio(request):
    request.session['heading'] = "Portfolio"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = portfolio.objects.filter(WORKER__LOGIN=request.session['lid'])
    return render(request, "worker/view portfolio.html", {'data': data})

def update(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view = portfolio.objects.get(id=id)
    return render(request, "worker/edit portfolio.html", {"data": view})

def update_post(request, id):
    portfolio.objects.filter(id=id).update(status="updated")

def delete(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    portfolio.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_portfolio#home'</script>")

#
def view_user_request(request):
    request.session['heading'] = "User Request"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = requests.objects.filter(PORTFOLIO__WORKER=request.session['wid'], status='pending')
    return render(request, 'worker/view user request.html', {'data': data})

def approve(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    requests.objects.filter(id=id).update(status="approved")

    return HttpResponse("<script>alert('approved');window.location='/approve_request#home'</script>")

def reject(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    requests.objects.filter(id=id).update(status="rejected")

    return HttpResponse("<script>alert('rejected');window.location='/view_user_request#home'</script>")

def approve_request(request):
    request.session['heading'] = "Approved Request"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = requests.objects.filter(PORTFOLIO__WORKER=request.session['wid'], status='approved')
    return render(request, 'worker/approve request.html', {'data': data})

def add_budget(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/add budget.html", {'id': id})

def add_budgetbuttonclick(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Budget = request.POST['textfield']
    if budget.objects.filter(REQUEST_id=id).exists():
        budget.objects.filter(REQUEST_id=id).update(status='pending', price=Budget)
    else:
        obj1 = budget()
        obj1.price = Budget
        obj1.REQUEST_id = id
        obj1.status = 'pending'
        obj1.save()
    return HttpResponse("<script>alert('Budget added');window.location='/view_status#home'</script>")

def view_status(request):
    request.session['heading'] = "Request Status"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = budget.objects.filter(REQUEST__PORTFOLIO__WORKER=request.session['wid'])
    return render(request, "worker/view status.html", {'data': data})

def add_material(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/add material.html", {'id': id})

def add_materialtbuttonclick(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Material = request.POST['m']
    Quantity = request.POST['q']
    Details = request.POST['d']

    obj = material()
    obj.material = Material
    obj.quantity = Quantity
    obj.details = Details
    obj.REQUEST_id = id
    obj.save()

    return HttpResponse("<script>alert('material added');window.location='/view_status#home'</script>")

def view_material(request, id):
    request.session['heading'] = "Material"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    view = material.objects.filter(REQUEST=id)
    return render(request, "worker/view_material.html", {'view': view})

def delete_material(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    m = material.objects.get(id=id)
    id = m.REQUEST_id
    m.delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_material/" + str(id) + "'</script>")

def add_advance_amount(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/add advance amount.html")

def add_advance_amountbuttonclick(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Advance_amount = request.POST['textfield']
    return HttpResponse("<script>alert('added');window.location='/view_advance_amount#home'</script>")

def view_advance_amount(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = payment.objects.filter(REQUEST=id)
    return render(request, "worker/view advance payment.html", {'data': data})

def view_complaint_from_user(request):
    request.session['heading'] = "Complaints"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = complaint.objects.filter(WORKER=request.session['wid'])
    return render(request, 'worker/view complaint from user.html', {'data': data})

def send_reply(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/send reply.html", {'id': id})

def send_replybuttonclick(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Reply = request.POST['textfield']
    complaint.objects.filter(id=id).update(reply=Reply, reply_date=datetime.datetime.now())

    return HttpResponse("<script>alert('reply sended');window.location='/view_complaint_from_user'</script>")

def change_password(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/change password.html")

def change_passwordbuttonclick(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    Old_password = request.POST['textfield']
    New_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']

    if Old_password == New_password:
        return HttpResponse("<script>alert('Enr password');window.location='/change_password'</script>")

    password1 = login.objects.filter(password=Old_password)
    if password1.exists():
        if New_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=New_password)
            return HttpResponse("<script>alert('password changed');window.location='/change_password'</script>")
        else:
            return HttpResponse("<script>alert('Incorrect password');window.location='/change_password'</script>")
    else:
        return HttpResponse("<script>alert('Invalid password');window.location='/change_password'</script>")

def view_review_and_rating(request):
    request.session['heading'] = "Review and Rating"
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = review.objects.filter(WORKER=request.session['wid'])
    return render(request, 'worker/view review and rating.html', {'data': data})

def forgot_password(request):
    return render(request,'forgot password.html')

def forgot_passwordbuttonclick(request):
    mail = request.POST['textfield']
    request.session['otp'] = str(random.randint(1000,9999))
    request.session['mail'] = mail

    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(projectemail, projectpassword)
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = projectemail
    msg['To'] = mail
    msg['Subject'] = 'otp'
    body = str(request.session['otp'])
    msg.attach(MIMEText(body,'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('otp sended successfully');window.location='/otp'</script>")


def otp(request):
    return render(request,"otp.html")

def otpbuttonclick(request):
    OTP = request.POST['textfield']

    new_password = login.objects.get(username = request.session['mail']).password

    if OTP == request.session['otp']:
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(projectemail, projectpassword)
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = projectemail
        msg['To'] = request.session['mail']
        msg['Subject'] = 'your password changed'
        body = new_password
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)

        return HttpResponse("<script>alert('passwurd changed successfully');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('invalid');window.location='/'</script>")


def workerlink(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "worker/index.html")



    #########user_chat######

def chatt(request, id):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    request.session['uid'] = id
    return render(request, 'worker/chat.html', {"id": id})

def chatsnd(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    d = datetime.datetime.now().strftime("%Y-%m-%d")
    m = request.POST['msg']
    obj = chat()
    obj.message_date = d
    obj.message_send = 'user'
    obj.WORKER_id = request.session['wid']
    obj.USER_id = request.session['uid']
    obj.message_reply = m
    obj.save()
    print(obj)
    v = {}
    if int(obj.id) > 0:
        v["status"] = "ok"
    else:
        v["status"] = "error"
    r = JsonResponse(v)
    return r

def chatrply(request):
    if request.session['login'] == "0":
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    res = chat.objects.filter(WORKER=request.session['wid'], USER=request.session['uid'])
    v = []
    if len(res) > 0:
        print(len(res))
        for i in res:
            v.append({
                'type': i.message_send,
                'message': i.message_reply,
                'name': 'Me',
                'id': i.USER.id,
                'upic': '/static/a.webp',
                'dtime': i.message_date,
                'tname': i.USER.name,
            })
        print(v)
        return JsonResponse({"status": "ok", "data": v})
    else:
        return JsonResponse({"status": "error"})
















