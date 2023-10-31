from django.shortcuts import render,redirect
from . import models
import random
import string

def generate_short_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not models.URL.objects.filter(short_code=code).exists():
            return code

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_code = generate_short_code()
        url = models.URL.objects.create(long_url=long_url, short_code=short_code)
        return render(request, 'modified_url/shorten_url.html', {'short_url': f'http://yourdomain.com/{short_code}'})
    return render(request, 'modified_url/shorten_url.html')

def redirect_original(request, short_code):
    url = models.URL.objects.get(short_code=short_code)
    return redirect(url.long_url)

def short_url_list(request):
    urls = models.URL.objects.all()
    return render(request, 'modified_url/short_url_list.html', {'urls': urls})
