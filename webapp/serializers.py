from rest_framework import serializers
from . models import students,racks

class studentsSerializers(serializers.ModelSerializer):

	class Meta:
		model = students
		fields = "__all__"


class racksSerializers(serializers.ModelSerializer):

	class Meta:
		model = racks
		fields = "__all__"

