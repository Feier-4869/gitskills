

from django.utils.deprecation import MiddlewareMixin

class My1(MiddlewareMixin):
    def process_request(self,request):

        print('--before---')



