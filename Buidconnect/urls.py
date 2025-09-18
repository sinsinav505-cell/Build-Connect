"""Buidconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Buildconnect import views

urlpatterns = [

    # path('',views.Login),
    # path('login_post',views.login_post),
    path('view_workers_approve',views.view_workers_approve),
    path('view_approved_workers',views.view_approved_workers),
    path('view_rejected_workers',views.view_rejected_workers),
    path('view_workers_portfolio',views.view_workers_portfolio),
    path('view_Complaint',views.view_Complaint),
    path('View_feed_back',views.View_feed_back),
    path('home_page',views.home_page),
    path('logout',views.logout),
    path('block/<id>',views.block),
    path('unblock/<id>', views.unblock),
    path('reason_submit',views.reason_submit),
    path('reason',views.reason),
    path('wapprove/<id>',views.wapprove),
    path('wreject/<id>',views.wreject),
    path('worker_portfolio/<id>',views.worker_portfolio),








    #-------------------uSER
    #-------------------uSER



    path('user_register',views.user_register),
    path('user_register_post',views.user_register_post),
    path('user_home',views.user_home),
    path('user_view_and_edit_profile',views.user_view_and_edit_profile),
    path('user_update/<id>',views.user_update),
    path('user_view_workers', views.user_view_workers),
    path('user_view_rating/<id>', views.user_view_rating),
    path('user_view_workers_portfolio/<id>',views.user_view_workers_portfolio),
    path('user_add_project_request/<id>', views.user_add_project_request),
    path('request_send_post/<id>', views.request_send_post),
    path('user_view_project_request_status', views.user_view_project_request_status),
    path('user_view_materials/<id>', views.user_view_materials),
    path('user_send_rating_to_worker/<id>', views.user_send_rating_to_worker),
    path('user_send_complaint/<id>', views.user_send_complaint),
    path('user_send_complaint_POST/<id>',views.user_send_complaint_POST),
    path('user_send_rating_to_worker_post/<id>',views.user_send_rating_to_worker_post),
    path('user_view_reply', views.user_view_reply),
    path('user_change_password_GET', views.user_change_password_GET),
    # path('user_change_password', views.user_change_password),
    path('user_change_password_POST',views.user_change_password_POST),
    path('user_approve_budget/<id>/<bid>',views.user_approve_budget),
    path('user_reject_budget/<id>/<bid>',views.user_reject_budget),
    path('payment_method/<amount>/<id>/<m>',views.payment_method),
    path('payment_post/<amount>/<id>',views.payment_post),
    path('chatt1/<id>',views.chatt1),
    path('offline/<id>',views.offline),
    path('online/<id>',views.online),
    path('chatsnd1',views.chatsnd1),
    path('default/<id>',views.default),
    path('chatrply1',views.chatrply1),
    path('user_send_feedback',views.user_send_feedback),
    path('send_feedbackbutton',views.send_feedbackbutton),

    path('register',views.register),
    path('registerbuttonclick',views.registerbuttonclick),
    path('view_and_edit_profile',views.view_and_edit_profile),
    path('view_and_edit_profilebuttonclick',views.view_and_edit_profilebuttonclick),
    path('update/<id>', views.update),
    path('update_post/<id>',views.update_post),
    path('delete/<id>', views.delete),
    path('add_portfolio',views.add_portfolio),
    path('add_portfoliobuttonclick',views.add_portfoliobuttonclick),
    path('edit_portfolio',views.edit_portfolio),
    path('edit_portfoliobuttonclick/<id>',views.edit_portfoliobuttonclick),
    path('view_portfolio',views.view_portfolio),
    path('view_user_request',views.view_user_request),
    path('approve/<id>',views.approve),
    path('reject/<id>',views.reject),
    path('approve_request',views.approve_request),
    path('add_budget/<id>',views.add_budget),
    path('add_budgetbuttonclick/<id>',views.add_budgetbuttonclick),
    path('view_status',views.view_status),
    path('add_material/<id>',views.add_material),
    path('view_material/<id>',views.view_material),
    path('delete_material/<id>',views.delete_material),
    path('add_materialtbuttonclick/<id>',views.add_materialtbuttonclick),
    path('add_advance_amount',views.add_advance_amount),
    path('add_advance_amountbuttonclick',views.add_advance_amountbuttonclick),
    path('view_advance_amount/<id>',views.view_advance_amount),
    # path('view_full_payment',views.view_full_payment),
    path('view_complaint_from_user',views.view_complaint_from_user),
    path('send_reply/<id>',views.send_reply),
    path('send_replybuttonclick/<id>',views.send_replybuttonclick),
    path('change_password',views.change_password),
    path('change_passwordbuttonclick', views.change_passwordbuttonclick),
    path('view_review_and_rating',views.view_review_and_rating),
    path('',views.index),
    path('Login',views.Login),
    path('login_post',views.login_post),
    path('workerlink',views.workerlink),

    path('chatt/<id>', views.chatt),
    path('chatsnd', views.chatsnd),
    path('chatrply', views.chatrply),
    path('forgot_password',views.forgot_password),
    path('forgot_passwordbuttonclick',views.forgot_passwordbuttonclick),
    path('otp',views.otp),
    path('otpbuttonclick',views.otpbuttonclick)
]