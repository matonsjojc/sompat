from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "copkeik"}
    return render(request, 'patients/index.html', context=context_dict)
