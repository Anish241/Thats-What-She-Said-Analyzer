from django.shortcuts import render
from . import predictor


# Create your views here.

def home(request):
    if request.method =='POST':
        sentence = request.POST.get('sentence')
        result = predictor.check(sentence)
        return render(request, 'result.html', {'result': result})
        
    return render(request, 'index.html')
