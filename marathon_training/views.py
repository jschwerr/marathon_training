from django.http import HttpResponseRedirect, HttpResponse

def root(request):
    return HttpResponseRedirect("/training_tracker/")