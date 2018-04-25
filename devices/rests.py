from django.db import models
from django.apps import apps
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from .forms import routerForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import router
import collections
import json

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def api_expose(request, api_method):
    rest_response = collections.OrderedDict()   
    params_list = list()
    params_list =  api_method.split("/")
    if request.method == 'GET':        
        if params_list[0] == 'routers':
            rest_response['api_method'] = params_list[0]
            if len(params_list) == 2:
                rest_response['type'] = params_list[1]
                routerlist = router.objects.filter(sapid = params_list[1]).values_list('hostname')
                rest_response['routes'] = routerlist
                print(routerlist)
            else:
                rest_response['Error'] = "Please check the request format. Request( method: routers, params:spaid (AG1/CSS))."
    if request.method == 'POST': 
        if params_list[0] == 'createrouters':            
            routercnt = router.objects.filter(Q(loopback = request.GET.get('loopback')) or Q(sapid = request.GET.get('hostname'))).count()
            if routercnt > 0:
                rest_response['Error'] = "Router is already exists."
            else:
                form = routerForm(request.GET)
                form.save()
                rest_response['Result'] = request.GET.get('hostname') + " Router Details has added successfully!"
        else:
            rest_response['Error'] = "Please check the request format.No method Name is " + api_method    
    if request.method == 'DELETE': 
        if params_list[0] == 'deleterouters':            
            ip = request.GET.get('hostname')
            idcnt = router.objects.filter(Q(hostname = ip)).count()
            
            if idcnt < 1:
                rest_response['Error'] = "No record exist"
            else:
                router.objects.get(hostname=ip).delete()
                rest_response['success'] = "successfully deleted Router " + ip
            
    if request.method == 'PUT':
        if params_list[0] == 'updaterouters':
            ip = request.GET.get('hostname')
            if not ip:
                rest_response['Error'] = "HostName/IP should is mandate field."  
            else:
                updateOb = router.objects.get(hostname=ip)
                if request.GET.get('sapid'):  
                    updateOb.sapid = request.GET.get('sapid')
                if request.GET.get('loopback'):
                    updateOb.loopback = request.GET.get('loopback')
                if request.GET.get('macaddress'):
                    updateOb.macaddress = request.GET.get('macaddress')
                updateOb.save()
                rest_response['success'] = "successfully update Router " + ip
                        
    return JSONResponse(rest_response)