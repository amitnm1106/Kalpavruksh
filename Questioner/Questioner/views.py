from django.shortcuts import render_to_response, render
from models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse


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

