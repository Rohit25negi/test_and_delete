from django.shortcuts import render
from django.views import View
from django.response import JSONResponse
# Create your views here.
import time

class APIView(View):
    def get_estimate(self,):
        return time.time()
    def get(self, request):

        try:
            ti = self.get_estimate()
        except:
            return JSONResponse({"message": ti})
        return JSONResponse({"message":"asdfsdaf"})


