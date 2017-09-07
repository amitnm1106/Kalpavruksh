from django.shortcuts import render_to_response, render
from models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from django.db.models import Sum


def landing_page(request):
    return render_to_response('html_templates/landing_page.html')

def get_questions(request, api_key):
    try:
        Tenant.objects.get(api_key=api_key)
    except ObjectDoesNotExist:
        return JsonResponse({
            "data": "API key not valid", 
            "status": False,
        })
    data = []
    for que in Question.objects.all():
        obj = {
            "title": que.title,
            "id": que.id,
            "answers": [{
                "answer": ans.body,
                "user": ans.user.name,
                "id": ans.id
            } for ans in que.answer_set.all()]
        }
        data.append(obj)
    return JsonResponse({
        "data": data, 
        "status": True,
    })


def dashboard_data(request):
    total_que = Question.objects.all().count()
    total_ans = Answer.objects.all().count()
    total_users = User.objects.all().count()

    return JsonResponse({
        "total_que": total_que,
        "total_ans": total_ans,
        "total_users": total_users,
        "tenent_api_counts": [{
            "count":  TApiCount.objects.filter(tenant=tenant).aggregate(Sum('request_count'))['request_count__sum'],
            "name": tenant.name,
            "api_key": tenant.api_key
        } for tenant in Tenant.objects.all()],
        "status": True,
    })