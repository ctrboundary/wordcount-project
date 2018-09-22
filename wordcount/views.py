
from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    word_dict={}
    for word in wordslist:
        if word in word_dict:
            #Increase
            word_dict[word]+=1
        else:
            #Insert
            word_dict[word]=1
    sortedwords= sorted(word_dict.items(),key=operator.itemgetter(1), reverse=True )

    return render(request,'count.html', {'fulltext':fulltext, 'count':len(wordslist), 'sortedwords':sortedwords})


def about(request):
    return render(request, 'about.html')
