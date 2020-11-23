# View - 로직 정의

from django.http import HttpResponse
import datetime

def current_daterime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s.</body></html>' %now
    return HttpResponse(html)

# 에러를 반환하고 싶은 경우
#   return HttpResponnseNotFound('<h1>Page not found(/h1)')