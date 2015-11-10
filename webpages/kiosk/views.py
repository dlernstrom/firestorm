# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from webpages.kiosk.models import Topic


def get_remarks():
    remarks_list = [
        "Whow, I loved Hack night.  It changed my life. --McKay",
        "Blue cheese?  who brings blue cheese to a GUN FIGHT? --Dirkus",
        "....um.... who's playing footsie with me under the table...Colby!, Im looking at you perv? :( --name withheld",
        "Does this moutain dew come in an Extra Large....  and cherry?  --Gavin"
    ]
    return remarks_list


def home(request):
    return render_to_response(
        'base.html', {'remarks': get_remarks()})


class TopicListView(ListView):
    model = Topic
    template_name = "topic_list.html"


# class TopicListView(ListView):
#     model = Vestiments
#     template_name = "vestiments_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(TopicListView, self).get_context_data(**kwargs)
#         context.update({'remarks': get_remarks()})
#         return context


class TopicDeleteView(DeleteView):
    model = Topic
    template_name = "topic_confirm_delete.html"
    success_url = reverse_lazy('view_topics')

    def get_context_data(self, **kwargs):
        context = super(TopicDeleteView, self).get_context_data(**kwargs)
        context.update({'remarks': get_remarks()})
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(TopicDeleteView, self).post(request, *args, **kwargs)


class TopicUpdateView(UpdateView):
    model = Topic
    template_name = 'form_edit_topic.html'
    fields = ['subject', 'description']


class TopicCreateView(CreateView):
    model = Topic
    template_name = 'form_add_topic.html'
    fields = ['subject', 'description', 'depth', 'suggested_by', 'suggested_date', 'user_interest', 'user_skill_level']
    success_url = reverse_lazy('view_topics')

    # def get_context_data(self, **kwargs):
    #     context = super(TopicCreateView, self).get_context_data(**kwargs)
    #     context.update({'remarks': get_remarks()})
    #     return context


def schedule(request):
    return render_to_response(
        'view_schedule.html', {'remarks': get_remarks()})


def reports(request):
    return render_to_response(
        'view_reports.html', {'remarks': get_remarks()})
