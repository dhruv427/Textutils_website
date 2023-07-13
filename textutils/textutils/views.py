from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    rmpunc = request.POST.get('removepunc', 'off')
    capital = request.POST.get('capitalize', 'off')
    Newlineremover = request.POST.get('Newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    flag = False
    onlycharcount = True
    if rmpunc == "on":
        flag = True
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text = analyzed
        onlycharcount=False

    if(capital == "on"):
        flag = True
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        text=analyzed
        onlycharcount = False

    if(Newlineremover == "on"):
        flag = True
        analyzed=""
        for char in text:
            if(char!='\n' and char!="\r"):
                analyzed = analyzed + char
            else:
                analyzed = analyzed + ' '
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}
        text = analyzed
        onlycharcount = False

    if (extraspaceremover == "on"):
        flag = True
        analyzed = ""
        for index,char in enumerate(text):
            if not (text[index]==' ' and text[index+1]==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        text=analyzed
        onlycharcount = False
    if(charcount == "on"):
        flag = True
        ctr = 0
        if(onlycharcount):
            analyzed = text
        for char in text:
            if(char!=' ' and char!='\n' and char!='\r'):
                ctr = ctr+1
        params = {'purpose': 'no of characters', 'analyzed_text': analyzed,'charctr':ctr}
        text = analyzed
    if(flag==False):
        return HttpResponse('<h3>You Must Select One Button</h3>')
    return render(request, 'analyze.html', params)
