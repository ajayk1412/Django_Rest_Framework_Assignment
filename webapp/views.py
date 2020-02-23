from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import students, racks
from . serializers import racksSerializers, studentsSerializers


def home_views(request):
	return render(request,'home.html')

class studentsList(APIView):

	def get(self, request):
		students1 = students.objects.all()
		sserialiser = studentsSerializers(students1, many = True)

		return Response(sserialiser.data)
	

	def post(self):
		pass


class rackssList(APIView):

	def get(self, request):
		racks1 = racks.objects.all()
		rserialiser = racksSerializers(racks1, many = True)

		return Response(rserialiser.data)
	

	def post(self):
		pass