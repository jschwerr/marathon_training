from django.http import HttpResponseRedirect, HttpResponse

# redirect root to training tracker app
def root(request):
    return HttpResponseRedirect("/training_tracker/")