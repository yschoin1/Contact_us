#-*- coding: utf-8 -*-

from django.db import models

# Model to store the contact us form input
class contact_us(models.Model):
	fullname = models.CharField('이름', max_length = 50)
	email = models.EmailField('이메일')
	subject = models.CharField('제목', max_length = 100)
	message = models.TextField('내용', max_length = 10000)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __unicode__(self):
		return self.fullname

	class Meta:
		verbose_name = 'Contact us'
		verbose_name_plural = 'Contact us'