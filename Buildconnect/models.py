from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class worker(models.Model):
     name = models.CharField(max_length=100)
     age = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     gender = models.CharField(max_length=100)
     pincode = models.CharField(max_length=100)
     post_office = models.CharField(max_length=100)
     place = models.CharField(max_length=100)
     latitude = models.CharField(max_length=100)
     longitude = models.CharField(max_length=100)
     skills = models.CharField(max_length=100)
     qualification = models.CharField(max_length=100)
     LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)

class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100)

    place = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)


class portfolio(models.Model):
    image1 = models.CharField(max_length=100)
    image2 = models.CharField(max_length=100)
    image3 = models.CharField(max_length=100)
    image4 = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    WORKER =  models.ForeignKey(worker,on_delete=models.CASCADE)


class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER =  models.ForeignKey(user,on_delete=models.CASCADE)
    WORKER =  models.ForeignKey(worker,on_delete=models.CASCADE)

class feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    LOGIN =  models.ForeignKey(login,on_delete=models.CASCADE)

class requests(models.Model):
    request = models.CharField(max_length=100)
    request_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    PORTFOLIO = models.ForeignKey(portfolio,on_delete=models.CASCADE)

class material(models.Model):
    material = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    REQUEST = models.ForeignKey(requests,on_delete=models.CASCADE)

class budget(models.Model):
    price = models.CharField(max_length=100)
    REQUEST = models.ForeignKey(requests,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class payment(models.Model):
    payment_mode = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    REQUEST = models.ForeignKey(requests,on_delete=models.CASCADE)

class review(models.Model):
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    review_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(worker, on_delete=models.CASCADE)

class chat(models.Model):
    message_send = models.CharField(max_length=100)
    message_reply = models.TextField(max_length=100)
    message_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    WORKER = models.ForeignKey(worker, on_delete=models.CASCADE)











#--------------------------------------------
