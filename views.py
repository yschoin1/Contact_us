#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from .forms import contact_us_form
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Contact us page view
def contact_us(request):
	# Import contact us form
	form = contact_us_form(request.POST or None)

	# Context to display with html
	context = {
		'header': 'Contact',
		'title': '여러분의 의견에 항상 귀 기울이는 노맛이 되겠습니다.',
		'form': form,
		'button': '보내기'
	}

	# If the form is valid, save the form and send confirmation email
	if request.method == 'POST':
		if form.is_valid():
			form.save()

			context = {
				'header': 'Contact',
				"title": "감사합니다!",
				'subtitle': '확인 후 바로 답장드리겠습니다.',
			}

			email = form.cleaned_data.get('email')
			message = form.cleaned_data.get('message')
			fullname = form.cleaned_data.get('fullname')
			subject = form.cleaned_data.get('subject')
			mail_message = """
이름: %s

이메일: %s

제목: %s

내용: %s
			""" % (fullname, email, subject, message)

			send_mail('nomat Contact us 내용', mail_message, 'splitterapps@gmail.com', ['splitterapps@gmail.com'], fail_silently=False)

			mail_message = '''
안녕하세요, 노맛을 이용해 주셔서 감사합니다!

아래는 문의해주신 내용입니다. 확인 후 바로 답장 드리겠습니다.


제목: %s

내용: %s


감사합니다!

nomat팀 드림
			''' % (subject, message)

			send_mail('nomat에 문의하신 내용입니다.', mail_message, 'splitterapps@gmail.com', [email], fail_silently = False)

			return render(request, 'jumbotronOnly.html', context)

	return render(request, 'form.html', context)




