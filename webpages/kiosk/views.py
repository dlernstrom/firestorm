# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from webpages.kiosk.models import *

def get_remarks():
    remarks_list = [
    "Whow, I loved Hack night.  It changed my life. --McKay",
    "Blue cheese?  who brings blue cheese to a GUN FIGHT? --Dirkus",
    "....um.... who's playing footsie with me under the table...Colby!, Im looking at you perv? :( --name withheld",
    "Does this moutain dew come in an Extra Large....  and cherry?  --Gavin"
    ]
    return remarks_list


def get_vestiments():
    return Vestiments.objects.all()


def get_vestiment(pk):
    return Vestiments.get(pk)


def home(request):
    return render_to_response(
        'base.html', {'remarks':get_remarks()})


def view_topics(request):
    return render_to_response(
        'view_edit_topic.html', {'remarks':get_remarks(),
                                 'vestiments':get_vestiments()})

def remove_topic(request, topic_key):
    topic = Vestiments.objects.filter(pk=topic_key).delete()
    return HttpResponseRedirect('/view/')


def update_topic(request, topic_key):
    topic = Vestiments.objects.get(pk=topic_key)
    if request.method == "GET":
        form = VestimentsForm(instance=topic)
        return render(
            request, 'form_edit_topic.html', { 'form' :form,
                                              'remarks':get_remarks()})
    elif request.method == "POST":
        form = VestimentsForm(request.POST or None, instance=topic)
        form.save()
        return HttpResponseRedirect('/view/')

def create_topic(request):
    if request.method == "GET":
        form = VestimentsForm
        return render(
            request, 'form_edit_topic.html', { 'form' :form,
                                              'remarks':get_remarks()})
    elif request.method == "POST":
        form = VestimentsForm(request.POST)
        form.save()
        return HttpResponseRedirect('/view/')

def schedule(request):
    return render_to_response(
        'view_schedule.html', {'remarks':get_remarks()})
   # return HttpResponse('some scheduli ng stuff goes here')


def reports(request):
    return render_to_response(
        'view_reports.html', {'remarks':get_remarks()})
    # return HttpResponse('some Reporting stuff goes here')


