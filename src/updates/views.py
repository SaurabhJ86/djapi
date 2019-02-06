import json
from django.core.serializers import serialize
from django.http import JsonResponse,HttpResponse

from django.shortcuts import render
from django.views.generic import View
from .models import Update
# Create your views here.

def update_model_detail_view(request):
	data = {
		"count":1000,
		"data":"Some data here"
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data,content_type='application/json')
	# return JsonResponse(data)


class SerializedDetailView(View):
	def get(self,request,*args,**kwargs):
		obj = Update.objects.get(id=2)
		data = obj.serialize()
		# data = serialize("json",[obj,],fields=("user","content"))
		# data = obj.serialize()
		return HttpResponse(data,content_type='application/json')


class SerializedListView(View):
	def get(self,request,*args,**kwargs):
		# qs = Update.objects.all()
		json_data = Update.objects.all().serialize()
		# data = serialize("json",qs)
		# data = serialize("json",qs,fields=("user","content"))
		# json_data = data
		# return JsonResponse(json_data)
		return HttpResponse(json_data,content_type='application/json')