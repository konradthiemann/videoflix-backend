from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
#from videoflix.settings import CACHE_TTL

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# Create your views here.
@cache_page(CACHE_TTL)
def index(request):
    return render(request, 'index.html')