from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request,'index.html')

def analyze(request):
    djText = (request.GET.get('text','default'))
    originalText = djText

    djRemovePunc = (request.GET.get('removePunc','off'))
    djupperCase = (request.GET.get('upperCase','off'))
    djextraSpaceRemove = (request.GET.get('extraSpaceRemover','off'))

    if(djRemovePunc == 'on'):
        newText = ''
        for char in djText:
            if char not in string.punctuation:
                newText += char
        djText = newText 

    if(djupperCase == 'on'):
        newText = ''
        for char in djText:
            newText += char.upper()
        djText = newText 
           
    if(djextraSpaceRemove == 'on'):
        newText = ''
        for index,char in enumerate(djText):
            if not(char[index] == ' ' and char[index+1] == ' '):
                newText += char
        djText = newText    
    
    params = {'userText' : originalText , 'analyzedText' : djText}
    return render(request,'analyze.html',params)