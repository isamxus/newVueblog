from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import ParamsSettings,ParamsContent
import json
import simplejson
from django.core import serializers
from ..base import SuccessMsg, FailedMsg, RequestHandler