from django.core.exceptions import ObjectDoesNotExist
from models import *
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, JsonResponse
from datetime import datetime, timedelta


class QuestionerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        try:
            api_key = request.path.split('/')[2]
            if api_key:
                current_date = datetime.now()
                try:
                    tenant = Tenant.objects.get(api_key=api_key)
                    tenant_api_count, created = TApiCount.objects.get_or_create(
                        tenant=tenant,
                        created__year=current_date.year, 
                        created__month=current_date.month, 
                        created__day=current_date.day, 
                    )
                    if tenant_api_count.next_request_time + timedelta(seconds=10) > current_date and tenant_api_count.request_count > 100:
                        return JsonResponse({
                            "message": "Try After 10 Seconds", 
                            "status": False,
                        })
                    else:
                        tenant_api_count.request_count += 1
                        tenant_api_count.next_request_time = current_date
                        tenant_api_count.save()

                except ObjectDoesNotExist:
                    return JsonResponse({
                        "message": "Invalid Api Key", 
                        "status": False,
                    })
        except Exception as e:
            pass
