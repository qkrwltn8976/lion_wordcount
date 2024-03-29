from django.shortcuts import render
from django.http import HttpResponse
import json
import operator
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    if request.is_ajax():
        full_text = request.GET['fulltext']
    
        word_list = full_text.split()
    
        word_dictionary = {}
    
        for word in word_list:
            if word in word_dictionary:
                # Increase
                word_dictionary[word] += 1
            else:
                # add to the dictionary
                word_dictionary[word] = 1

        word_sort = {}
        word_sort = sorted(word_dictionary.items(), key=operator.itemgetter(0))

        for key, value in word_sort:
            print("++++++++++"+key+"++++++"+str(value))

        data = {'fulltext': full_text, 'total': len(word_list), 'dictionary': list(word_dictionary.items()), 'sort': list(word_sort)}
        
        return HttpResponse(json.dumps(data), "application/json")
        
        
    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
