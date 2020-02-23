from django.db import models

# Create your models here.
class students(models.Model):
	firstname = models.CharField(max_length = 10)
	lastname = models.CharField(max_length = 10)
	roll_number = models.IntegerField()

	def __str__(self):
		return self.firstname
class racks(models.Model):
	student = models.ForeignKey(students, on_delete=models.DO_NOTHING,blank=True, default = None)
	rack_name = models.CharField(max_length = 10)

	def __str__(self):
		return self.rack_name