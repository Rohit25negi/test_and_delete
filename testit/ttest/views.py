from django.views import View
from django.views.generic.base import TemplateView
from django.http import JsonResponse
# Create your views here.
import time
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import connection

@method_decorator(csrf_exempt, name='dispatch')
class APIView(View):
    def post(self, request):
        data = list()
        with connection.cursor() as cursor:
            cursor.execute(request.POST['sql_query'])
            data = cursor.fetchall()
        
        return JsonResponse({"message":data})



class TView(TemplateView):

    def get(self, request):
        template = loader.get_template('form.html')
        return HttpResponse(template.render({}, request))