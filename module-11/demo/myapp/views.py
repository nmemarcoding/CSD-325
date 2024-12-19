from django.http import HttpResponse

def home(request):
    return HttpResponse("Memarzadeh says Hello!")
