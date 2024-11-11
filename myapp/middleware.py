import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.cache import cache
from django.utils import timezone
logger=logging.getLogger('__name__')


class Ratelimitermiddleware(MiddlewareMixin):
    RATE_LIMIT=20
    TIME_WINDOW=60
    def process_request(self,request):
        user_id=request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
        request_key=f"rate_limit_{user_id}"
        request_count=cache.get(request_key,0)
        if request_count>=self.RATE_LIMIT:
            return JsonResponse({"error":"Rate limit exceeded"})
        
        cache.set(request_key,request_count+1,timeout=self.TIME_WINDOW)

class Requestcountermiddleware:
    request_counter=0
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        Requestcountermiddleware.request_counter+=1
        current_time=timezone.now()
        logger.info(f"Request number {Requestcountermiddleware.request_counter} received at {current_time}")
        response=self.get_response(request)
        return response

