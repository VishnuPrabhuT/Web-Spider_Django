from django.shortcuts import render
from django.views import View

import pdb;
from bs4 import BeautifulSoup

import requests
import sys

from django.http import HttpResponseRedirect

from .models import Requester
from .forms import RequesterForm
# Create your views here.


class Index(View):
	def get(self,request):
		form = RequesterForm()
		data_list=Requester.objects.order_by('-name')
		context={'form' : form,'data_list':data_list}
		return render(request,'profiles/index.html',context)
	def post(self,request):
		URL='https://infoed.clemson.edu/login.asp'
		form = RequesterForm(request.POST)
		if form.is_valid():
			fieldText=form.cleaned_data['field']
			departmnetText=form.cleaned_data['department']
			nameText=form.cleaned_data['name']
			form.save()
		data_list=Requester.objects.order_by('-name')
		login_data = {
        'username': 'vthirug',
        'password': 'in@the@en',
        'submit': 'Login',
    	}
		session = requests.session()
		r = session.post(URL,data=login_data)
		temp = session.get(URL)
		oldStr='High%20Performance%20Computing'
		newStr=fieldText		
		newStr=newStr.replace(' ','%20')		
		newURL='https://infoed.clemson.edu/Webportal/g3.asp?PageID=&direction=&reportall=0&search=1&FontColor=%23292929&FontColor2=midnightblue&BGColor=%23F3EBCB&BGColor2=%23F2EACA&BorderColor=%2380694D&searchFielda=k&a=High%20Performance%20Computing&curr_pid=&textname=a&andornota=and&searchFieldb=k&b=&curr_pid=&textname=b&andornotb=and&searchFieldc=k&c=&curr_pid=&textname=c&andornotc=and&searchFieldd=k&d=&curr_pid=&textname=d&andornotd=and&searchFielde=k&e=&curr_pid=&textname=e&=Add%20Term&=Search&searchArea=L&=Clear&resultsper=100&=More%20Actions'
		newURL=newURL.replace(oldStr,newStr)
		r = session.get(newURL)
		soup = BeautifulSoup(r.text, 'html.parser')
		temp=soup.find_all('font')
		tempStr=''
		size=len(temp)
		array=['']
		for t in temp:
			size-=1
			if t is not None:
				tempStr+=t.get_text()
				tempStr=tempStr.replace('Phone:',' || Phone - ')
				tempStr=tempStr.replace('Email:',' || Email - ')
				tempStr=tempStr.replace('Title:',' || Title - ')
				tempStr=tempStr.replace('Clemson University','| Clemson University')
				if size%3==0:
					array.append(tempStr)
					tempStr=''
		
		# for x in soup.find_all('font'):
		# 	if x.string is not None:
		# 		x=x.string.strip(' ')
		# 		x=x.replace('\n','')
		# 		x=x.replace('\t','')
		# 		x=x.replace('\r','')
		# 		# x=x.replace(' ','')
		# 		array.append(x)
		context={'form' : form,'array':array,'soup':tempStr}
		return render(request,'profiles/index.html',context)



def hello(request):
	return render("<h2>Hello, world. You're at the polls index.</h2>")