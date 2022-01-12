from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here. создате тут свои модели

class Topic(models.Model): #если назвать NameTopic, то напишет Select name topic to change. разделения большими буквами как пробел работает в подсказке.
	"""Тема, которую изучает пользователь"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
 
	def __str__(self):
#Возвращает строковое представление модели."""
		return self.text
