
from django.shortcuts import render

def home (r):
      return render(r,'home.html')
def reverse (request):
      user_text = request.Get['username']
      reversed_text = user_text [::-1]
      return render(request,'revers.html',{'word': reversed_text})