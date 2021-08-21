# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if newlineremover == "on":

        analyzed = ""

        for char in djtext:
            if char != "\n" and char!= "\r":

                analyzed = analyzed + char

        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}

        # return render(request, 'analyze.html', params)
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):

                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra sapces', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext =analyzed

    if charcounter == "on":
            analyzed = len(djtext) - djtext.count(" ")

            params = {'purpose': 'character counter', 'analyzed_text': "Number of characters in {} are {}".format(djtext,analyzed)}


    if(removepunc !="on" and charcounter !="on"and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on"):

        return HttpResponse("error")

    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")

