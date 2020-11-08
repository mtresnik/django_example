from django.views.generic import TemplateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import resolve
import base64
import os
import json

class MainView(TemplateView):

	template_name = 'dicts/index.html'

	def dummy(self, request):
		example_dict = {
			"name" : "Mike",
			"age" : 23,
			"weight": 176.3,
			"cats" : True
		}

		return render(
			request = request,
			template_name=self.template_name,
			context={
				"example_dict" : json.dumps(example_dict)
			}
			)

	def get(self, request):
		return self.dummy(request)

	def post(self, request):
		return self.dummy(request)