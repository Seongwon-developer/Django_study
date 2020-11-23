# URLconf - URL 정의

# url과 뷰를 매핑 => URLconf

from django.urls import path, re_path

# from . import views

urlpatterns = [
    path('articles/2003/', views.special_case_2003),        # (url, 부분 처리 함수(뷰))
    path('articles/<int:year>/', views.year_archive),       # <type:name>
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),        # 정규 표현식 사용 - 더 정교하게 정의하고자 할 때
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$]', views.article_detail)
]
     
# url이 'articles/2018'이면 views.year_archive(request, year:2018)처럼 호출
# <> : Path Converter
#   str : '/'를 제외한 모든 문자, int : 정수, slug : slug 형식 문자열(ex. ASCII, 숫자, GKDLVMS, 밑줄로만 구성)
#   uuid : UUID 형식 문자열, path : '/'를 포함한 모든 문자열 (url 전체를 추출할 때 사용)

# . : 모든 문자 하나, ^ : 문자열 시작, $: 문자열 끝, [] : 괄호 안에 있는 문자만(안에 ',' 사용x)
# [^ ] : 괄호 안에 있는 문자 제외한 문자 하나, * : 0번 이상 반복(={0,}), + : 1번 이상 반복(={1,})
# ? : 0번 또는 1번 이상 반복(={0,1}), {n} : n번 반복, {m,n} : m번 이상 n번 이하 반복
# | : 또는, '[a-z] : a~z 사이에서 1개, \w : 영문, 숫자 또는 밑줄(_) 1개(=[0-9a-zA-Z]), \d : 숫자 한개(=[0-9])