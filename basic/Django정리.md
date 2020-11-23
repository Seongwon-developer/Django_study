# Django

## 질문, 선택지, 투표 

- ```
  C:~>django-admin startproject mysite
  ```

  - mysite 디렉토리 생성

- ```
  C:~>move mysite startsite
  ```

  - mysite 상위 디렉토리 startsite로 이름 변경

- ```
  C:~>startsite>python manage.py startapp polls
  ```

  - polls 애플리케이션 개발에 필요한 디렉토리 생성

- ```
  C:~>startsite>mysite>notepad settings.py
  ```

  - settings.py 메모장 파일로 열기

  - ALLOWD_HOSTS=[]
    - DEBUG=TRUE 개발모드
    - DEBUG=FALSE 운영모드
    - ALLOWD_HOSTS = ['localhost', 172.18.102.67]
      - 써도 되고 안써도 되고
      - 안쓰면은 개발모드로 인식하여 상관 없음
      - ip가 두개라면은 ip, 'localhost', ip 형식으로 작성

- settings.py

  - ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    	'polls.apps.PollsConfig'		# 장고가 설정 클래스를 잘 찾게 하기위해 추가
    ]
    ```

  - ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ```

    - 이 부분을 보면 sqlite3 데이터베이스 형식을 사용했다는 것을 알 수 있음

  - ```
    TIME_ZONE = 'UTC'
    ```

    ```
    TIME_ZONE = 'Asia/Seoul'
    ```

    - 세계 표준시를 한국 표준시로 변경

- ```
  C:~>startsite>mysite>python manage.py migrate
  # 모든 앱에서 migrate
```
  
  - 데이터베이스 파일 생성
  
- DB가 필요없어도 그냥 해야하는 것 반드시
  
  - db.sqlite3 파일 생성
  
  - ```
    > python manage.py makemigrations polls
    # polls의 모델링 클래스 migrate
    ```
  
  - ```
    > python manage.py sqlmigrate 0001
    # 모델링 클래스 현황
    ```
  
    
  
- 새로운 cmd 창을 열어서 서버 실행할 것

  ```
  C:~>startsite>mysite>python manage.py runserver 0.0.0.0:8000	// 또는 0:8000
  ```

  - ​	서버 실행
  - 주소 : 'localhost:8000' or '자신의 ip주소:8000'

- 'localhost:8000/admin' 들어가면 로그인 화면창이 뜸

  - 유저 등록하기

    ```
    C:~>stratsite>python manage.py createsuperuser
    ```

    - username, email address, password 입력

- 데이터베이스 생성

  - 반드시 models.py와 admin.py 같이 해줘야 한다.

  - startsite/polls/models.py

    ```
    from django.db import models
    
    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
    
        def _str_(self):
            return self.question_text
    
    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    
        def __str__(self):
            return self.choice_text
    ```

    - 하나의 클래스는 하나의 테이블
      - Question은 id를 더하여 3개의 컬럼, Choice는 id를 더하여 4개의 컬럼
      - def _ str _ (self): 는 사이트에서 테이블 명을 보여주기 위한 것 

  - startsite/polls/admin.py

    ```
    from django.contrib import admin
    from polls.models import Question, Choice
    
    admin.site.register(Question)
    admin.site.register(Choice)
    ```

    - admin 사이트에서 Question과 Choice를 보여주기 위해 필요

  - ```
    C:~>startsite>python manage.py makemigrations
    C:~>startsite>python manage.py migrate
    ```

    - makemigreations : /polls/migrations 디렉토리 생성
    - migrate 데이터베이서 수정 사항 알림

- startsite/mysite/urls.py

  ```
  from django.contrib import admin
  from django.urls import path
  
  urlpatterns = [
      path('admin/', admin.site.urls),
  ]
  ```

  ```
  from django.contrib import admin
  from django.urls import path
  from polls import views
  
  urlpatterns = [		# 위에서 아래로 순서에 맞춘다.
      path('admin/', admin.site.urls),
      path('polls/', view.index, name='index'),	# 이 밑으로 url/뷰 매핑
      path('polls/<int:question_id>/', views.detail, name='detail'),
      path('polls/<int:question_id>/results/', view.results, name='results'),
      path('polls/<intLquestion_id>/vote/', view.vote, name='vote'),
  ]
  ```

  - path 함수 : route, view 2개의 필수 인자, name. kwargs 2개의 선택 인자
    
    - route : url 패턴 표현, url스트링이라고도 함
    - view : 스트링에서 추출된 항목이 뷰 함수의 인자로 전달
    - name : 스트링에 이름 부여
    
  - kwargs : 스트링에서 추출된 항목 외에 추가적인 인자를 뷰 함수에 전달 시, 파이썬 사전 타입으로 인자 정의
    
  - startsite/polls/urls.py를 만들어 똑같이 입력해주는 것이 나중에 더 효울적인 개발 가능

    startsite/polls/urls.py

    ```
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('polls/', views.index, name='index'),
        path('polls/<int:question_id>/', views.detail, name='detail'),
        path('polls/<int:question_id>/results/', views.results, name='results'),
        path('polls/<intLquestion_id>/vote/', views.vote, name='vote'),
    ]
    ```

  - 개발 순서에서도 urls.py 다음 views.py 순서로 (오류에 당황하지 말 것)

  - 다음처럼 변경하는 것이 더 효율적 : polls에 있는 것을 include 하여 다 가져온다. 

    startsite/mysite/urls.py
    
    ```
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('polls/', include('polls.urls')),
    ]
    ```
    
    startsite/polls/urls.py
    
    ```
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/', views.detail, name='detail'),
        path('polls/<int:question_id>/results/', views.results, name='results'),
        path('polls/<intLquestion_id>/vote/', views.vote, name='vote'),
    ]
    ```

- template, template/polls 디렉토리 생성

  ```
  C:~>stratsite/polls> mkdir templates
  C:~>stratsite/polls> mkdir templates/polls
  ```
  
  C:~>stratsite/polls/templates/polls/index.html
  
  ```
  {% if latest_question_list %}
    <ul>
    {% for question om latest_question_list %}
    <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
  {% else %}
    <p>No polls are available.</p>
  {% endif %}
  ```
  
    - latest_question_list 객체 : index() view 함수에서 넘겨주는 파라미터
    
      latest_question_list 객체의 내용을 순화하면서 question_text를 순서 없는 리스트로 화면에 출력
    
      - ul, li : 태그 역할
      
      
  
    또한 각 텍스트에 URL 링크 연결
      
    - a href : 속성 역할
      
  - URL 링크는 /polls/3/과 같은 형식
  
  - 만약 latest_question_list 객체에 내용이 없다면 "No polls ~" 내용 출력
  
- startsite/polls/view.py

  ```
  from django.shortcuts import render
  from polls.models import Question
  
  def index(request):
  	# Question 테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 5개의 최근 객체를 가져온다
  	# Question이 에러가 발생하지만 무시해도 된다.
      latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
      # 템플릿에 사용될 변수명과 그 변수명에 해당하는 객체를 매핑
      context = {'latest_question_list': latest_question_list}
      # 'polls/index.html'에 context 변수를 적용
      return render(request, 'polls/index.html', context)
  ```

  render = loader와 HttpRespose 
  
  loader : 지정 경로에서 템플릿을 찾는다.
  
  HttpRespose : 문자열, 반복자 전달, 헤더 필드 설정, 
  
- startsite/polls/templates/polls/detail.html

  ```
  # <h1> 사이즈의 제목
  <h1>{{ question.question_text }}</h1>
  
  # 에러가 있으면 굵은 문자로 에러 메세지 표시
  {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
  
  # form에 입력된 데이터는 post 방식으로 polls/vote로 보낸다
  <form action ="{% url 'polls:vote' question.id %}" method="post">
  
  # 보안을 위해 장고에서 제공하는 기능
  {% csrf_token %}
  
  {% for choice in question.choice_set.all %}
      <input type="radio" name="choice" id="choice{{ forlooop.counter }}" value="{{choice.id }}" />
      <label for = "choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
      {% endfor %}
      <input type="submit" value="vote" />
  </form>
  ```

  forloop.counter : 반복문 실행 횟수 계산

  https://dasima.xyz/html-label/ 참고

- startsite/polls/view.py

  추가

  ```
  # get~ 추가
  from django.shortcut import renderm det_object_or_404
  
  def detail(request, question_id):
      question = get_object_or_404(Question, pk=question_id)
      return render(request, 'polls/detail.html'), {question:question}
      
  def vote(request, question_id):
      question = get_object_or_404(Question, pd=question_id)
    try:
          selected_choice = question.choice_set.get(pk=request.POST['choice'])
      except (KeyError, Choice.DoesNotExist):
          return render(request, 'polls/detail.html', {
              'question': question,
              'error_message': "You didn't select a choice",
          })
      
      else:
          selected_choice.votes += 1
          selected_choice.save()
          return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
  
  def results(request, question_id):
      question = get_object_or_404(Question, pk=question_id)
      return render(request, 'polls/results.html', {'question': question})
  ```
  
  - get_object_or_404 : 첫 번째 인자 - 모델 클라스(테이블 검색), 두 번쨰 인자 - 검색 조건
    검색 조건에 맞는 값이 없으면 에러 출력
  - 예외 처리 순서 - try -> except -> else -> finally
    - else : except가 실행되지 않았을 경우(즉, 에러가 발생하지 않았을 경우) 실행
    - finally : 에러와는 상관없이 그냥 실행
  
- startsite/polls/templates/polls/results.html

  ```
  <h1>
      {{ question.question_text }}
  </h1>
  
  <ul>
      {{% for question in question.choice_set.all %}}
      <li>
          {{ choice.choice_text }} - {{choice.votes }} vote{{ choice.votes|pluralize}}
      </li>
      {{% endfor %}}
  </ul>
  
  <a href="{% url 'polls:detail' question.id %}">
      Vote again?
  </a>
  ```

  vote{{ choice.votes|pluralize}} : vote 값에 따라 뒤에 s를 불일지 말지(단수 복수)

  localhost:8000/admin/ 에 들어가서 Question, Choice 추가 하고 /polls/에 들어가기


- 필드 순서 변경

  - localhost:8000/polls/question/1/change
    - 원래 순서 : question_text, date published
    - 바꿀 순서 : date_published, question_text

  - startsite/polls/admin.py
    - 추가

      ```
      class QuestionAdmin(admin.ModelAdmin):
          # 필드 순서 변경, Fields가 아니라 field 소문자로 입력해야함
          fields = ['pub_date', 'question_text']
      ```

- 필드 분리와 접기

  - startsite/polls/admin.py

    - class QuestionAdmin 수정

      ```
      class QuestionAdmin(admin.ModelAdmin):
          fieldsets = [
              # (필드 제목, 필드 안 내용)
              ('Question Statement', {'fields':['question_text']}),
              ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
          ]
      
      ```

- 질문과 선택지를 한 화면에서 변경하기

  - startsite/polls/admin.py 수정

    ```
    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 2
    
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            # (필드 제목, 필드 안 내용)
            (None, {'fields':['question_text']}),
            ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),
        ]
        inlines = [ChoiceInline]
    ```

    localhost:8000/admin/polls/ 에서 Question에 들어가 하나를 택하면 질문과 선텍지를 한 번에 변경 가능하다.

  - 테이블 형식으로 보여주기

    startsite/polls/admin.py 수정

    ```
    class ChoiceInline(admin.TabularInline):
    ```

- polls/question 웹에 레코드 리스트 컬럼 지정하기

  class QuestionAdmin에 추가

  ```
  list_display = ('question_text', 'pub_date')
  ```

- polls/question 웹에 필터 사이드바 추가

  class QuestionAdmin에 추가

  ```
  # 'pub_date' 변수에 맞는 필터 사이드 바 추가
  list_filter = ['pub_date']
  ```

- admin 사이트 템플릿 수정

  mysite/templates/admin 디렉토리 생성

  base_site.html 파일을 만든 디렉토리에 복사

  ```
  C:~/mysite> mkdir templates
  C:~/mysite> mkdir templates/admin
  C:~/mysite> copy python/Lib/site_packages.django/contrib.admin/templates/admin/base_site.html templates/admin
  ```

  mysite/settings.py

  수정

  ```
  TEMPLATES = [
  	{
  		'DIRS': [os.path.join(BASE_DIR, 'templates')],
  	}
  ]
  ```

  base_site.html

  수정 -> 제목 변경

  ```
  <h1 id="site-name">
  	<a href="{% url 'admin:index' %}">
  		{{ site_header|default:_('Django administration') }}
  	</a>
  </h1>
  ```

  ```
  <h1 id="site-name">
  	<a href="{% url 'admin:index' %}">
  		Seongwon-developer's Site
  	</a>
  </h1>
  ```

- 장고 쉘을 이용

  - Create - 데이터 생성/입력

    SQL 용어 

    save() : INSERT

    ```
    C:~/startsite>python manage.py shell
    >>> from polls.models import Question, Choice
    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new", pub_date=timezone.now())
    >>> q.save()
    ```

  - Read - 데이터 조회

    SQL 용어

    QuerySet(objects.all) : SELECT

    filter : WHERE, 조건에 맞는 것을 가져옴

    exclude : 조건을 제와한 것을 가져옴

    ```
    >>> question.objects.all()
    <QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>, <Question: what's new>]>
    ```

    question.objects.all() : 은 models.py의 str() 함수의 return 값으로 뼏

    ```
    >>> Question.objects.filter(
    ...		question_text_startswith='What'
    ...	).exclude(
    ...		pub_date_gte = datetime.date.today()
    ...	).filter(
    ...		pub_date_gte = datetime(2005,1,30)
    ...	)
    ```

  - Update - 데이터 수정

    SQL 용어

    이미 있는 데이터를 수정하여 save() : UPDATE

    여러 개를 수정할 경우 update() 함수 사용

    ```
    >>> q.question_text = "What is your favorite hobby?"
    >>> q.save()
    >>> Question.objects.filter(pub_date__year=2017).update(question_text='Everything is the same')
    ```

  - Delete - 데이터 삭제

    SQL 용어

    delete() : DELETE

    ```
    >>> Question.objects.filter(pub_date__year=2018).delete()
    >>> Question.objects.all().delete()
    ```


  - 데이터 선택

    ```
    >>> Question.objects.filter(id=5)
    <QuerySet [<Question: What is your hobby?>]>
    >>> Question.objects.filter(pk=5)	# 윗 줄과 같은 것을 의미한다.
    <Question: What is your hobby?>
    ```

    - 생성(id=1) - 삭제(id=1) - 생성(id=2)

      - id=1이 비어있으므로 비어있는 공간으로 보일 수 있지만 실제로는 그런 것이 아니다.

        ​	-> id 값은 모르는 것이라 생각할 것

    ```
    >>> q = Question.objects.get(pk=5)
    >>> q.choice_set.all() 
    <QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>]>
    ```

  - 참조하는 테이블 데이터 생성

    ```
    >>> q.choice_set.create(choice_text = 'Sleeping', votes = 0)
    <Choice: Sleeping>
    >>> q.choice_set.all()
    <QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>, <Choice: Sleeping>]>
    ```

  - 속성 값 갯수

    ```
    >>> q.choice_set.count()
    4
    ```

## 템플릿 시스템

- 템플릿 변수

  ```
  {{ variable }}
  ```

  - .(도트) 형식 사용 가능 (파이썬과는 조금 다르다)
    - ex. 'foo.bar'
      - 다음 순서로 해석
        - foo가 사전 타입일 경우 -> foo['bar']
        - foo의 속성 안에 bar라는 속성이 있는지
        - foo가 리스트인 경우

  - 템플릿 시스템은 정의가 되어 있지 않은 변수를 사용하는 경우, 빈 문자열로 채줘주며, 이 값을 변경하려면 settings.py 파일레 다음과 같은 속성을 지정해야 한다.

    - ```
      TEMPLATE_STRING_IF_INVALID
      ```

- 템플릿 필터

  - |(shift + \\)를 사용

    - 소문자로 바꿔주는 필터

      ```
      {{ name|lower}}
      ```

    - 필터를 체인에 연결

      text 변수값 중에서 특수 문자를 이스케이프 해주고 그 결과 HTML <p> 태그를 붙인다.

      ```
      {{ text|escape|linebreak }}
      ```

    - 필터는 인자를 가질 수 있다

      다음은 bio 변수값 중에서 30개의 단어만 보여주고, 줄 바꿈 문자는 모두 없애준다.

      ```
      {{ bio|truencatewords:30 }}
      ```

    - 필터의 인자에 빈칸이 있는 경우 따옴표로 묶어준다.

      만일 list가 ['a','b','c']라면 결과는 "a//b//c"가 된다.

      ```
      {{ list|join:"//" }}
      ```

    - value 변수값이 False이거나 없는 경우, "nothing"으로 보여준다.

      ```
      {{ value|defult:"nothing" }}
      ```

    - value 변수갑의 길이를 반환

      value가 스트링이나 리스트인 경우도 가능

      ex. ['a','b','c']인 경우 값은 3

      ```
      {{value|length}}
      ```

    - value 변수값에서서 HTML 태그를 모두 없앤다. 100%는 아니다.

      ```
      {{ value|striptags }}
      ```

    - 복수 접미사 필터

      ```
      {{ value|plirlize:'es'}}
      {{ value|plirlize:'ies'}}
      ```

    - 더하기 필터

      변수로도 사용 가능

      ```
      {{ value|add:'2' }}
      ```

- 템플릿 태그

  - {% for %}
  
    ```
    <ul>
    {% for athlete in athlete_list %}]
    	<li>{{ athlete.name }}</li>
    {% endfor%}
    </ul>
    ```
  
    athlete_list애 들어있는 athlete을 순회하면서 athlete.name 을 보여주는 문장
  
    - 사용할 수 있는 변수
      - forloop.counter : 현재까지 루프를 실행한 루프 카운트 1부터
      - forloop.counter() :                              ''                              0부터
      - forloop.recounter : 루프 끝에서 현재가 몇 번쨰인지 카운트 1부터
      - forloop.recounter() :                                   ''                              0부터
      - forloop.first : 루프에서 첫 번째 실행이면 True
      - forloop.last : 루프에서 마지막 실행이면 True
      - forloop.parantloop : 중첩된 루프에서 루프 바로 상위의 루프를 의미
  
  - {% if  %}
  
    ```
    {% if athlete_list %}
    	Number of athletes: {{ ahtlete_list|length }}
    {% elif athlete_in_locker_room_list %}
    	Athlete should be out of the locker room soon!
    {% else %}
    	No athlete
    {% endif %}
    ```
  
    {% 변수 %} 가 True -> 밑에 문장 출력
  
    대부분의 필터는 스트링을 반환하므로 산술 연산 불가능 but length만 가능
  
    ```
    {% if athlete_list|length > 1 %}
    ```
  
    and, or, not, and not, ==, !=, <, >, >=, <=, in, not in 연산자 사용 가능
  
  - {% csrg_token  %}
  
    ```
    <form action="." method="post">{% csrf_token %}
    ```
  
    장고는 내부적으로 CSRF 토큰값의 유효성 검증
  
    검증 실패 -> 403에러
  
    토큰값 유출 방지 -> 외부 URL로 보내는 <form>에 사용x
  
  - {% url %}
  
    ```
    <form action="{% url 'polls:vote' question.id  %}" method="post">
    ```
  
    하드코딩 방지 목적
  
    하드코딩하는 경우
  
    ```
    <form action="/polls/3/vote/" method="post"
    ```
  
    ​	url 변경하는 경우 모든 html 파일 수정해야함
  
    사용 형식
  
    ```
    {% url 'namespace:view-name' arg1 arg2 %}
    ```
  
    namespace : urls.py 파일의 include() 함수 또는 app_name 변수에 정의한 이름 공간 이름
  
    view_name : urls.py 파일에서 정의한 URL 패턴 이름
  
    argN : 뷰 함수에서 사용하는 인자로, 없을 수도 있고 여러 개인 경우 빈칸으로 구분
    
  - {% with %}
  
    ```
    {% with total=business.emloyees.count %}
    	{{ total }} people works at business
    {% endwith %}
    ```
  
     특정 값을 변수에 저장해두는 기능
  
  - {% load %}
  
    ```
    {% load somelibrary apckage.otherlibrary %}
    ```
  
    사용자 정의 태그 및 필터 로딩
  
    파이썬 import. C언어 include
  
- 템플릿 주석

  {##} : 한줄

  {% comment %} ~ {% endcomment %} : 여러줄, 중첩 불가

- HTML 이스케이프

  ```
  name = <b>username
  ```

  ```
  Hello, {{name}}
  ```

  출력 : Hello, <b>username
  
  이스케이프 문자
  
  ```
  < : &lt;
  > : &gt;
  ' : &39;
  " : &quot;
  & : &amp;
  ```
  
  이스케이프 적용
  
  ```
  name = &lt;b&gt;username
  ```
  
  safe 필터를 사용한 이스케이프
  
  ```
  Hello, {{name|safe}}
  ```
  
  {{% autoescape %}}
  
  ```
  {{% autpescape off %}}
  Hello {{name}}
  {% endautoescape %}
  ```
  
  인자에 해당하는 스트링 리터럴도 이스케이프 시켜줘야한다.
  
  ```
  {{ date|default:"3<5"}}  (x)
  {{ date|default:"3&lt;5"}}  (o)
  ```

- 템플릿 상속

  {% block %} :

  부모 템플릿은 자식 템플릿으로 상속해줄 부분 지정

  자식 템플릿은 block에 입력 

  - 부모 템플릿

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<link rel="stylesheet" href="style.css" />
    	<title>{% block title %}My amazing site{%% endblock }</title>
    </head>
    
    <body>
    	<div id="sidebar">
    		{% block sidebar %}
    		<ul>
    			<li><a href="/"Home></a></li>
    			<li><a href="/Blog">Blog</a></li>
    		</ul>
    		{% endblock %}
    	</div>
    	
    	<div id="content">
    		{% block content %}{% endblock %}
    	</div>
    </body>
    </html>	
    ```

  - 자식 템플릿

    ```
    {% extends "base.html" %}
    
    {% block title %}My amazing block{% endblock %}
    {% block content %}
    {% for entry in blog.entries %}
    	<h2>{{ entry.title }}</h2>
    	<p>{{ entry.body }}</p>
    {% endfor %}
    {% endblock %}
    ```

  - 자식 템플릿 렌더링 결과

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
    	<link rel="stylesheet" href="style.css" />
    	<title>My amazing blog</title>
    </head>
    
    <body>
    	<div id="sidebar">
    		<ul>
    			<li><a href="/">Home</a></li>
    			<li><a href="/blog">Blog</a></li>
    		</ul>
    	</div>
    	
    	<div id="content">
    		<h2>Entry one</h2>
    		<p>This my first entry.</p>
    		
    		<h2>Entry two</h2>
    		<p>This is my second entry.</p>
    	</div>
    </body>
    </html>
    ```

  - 상속의 3단계

    1. 사이트 전체의 룩앤필을 담고 있는 base.html 생성

    2. 사이트 하위의 섹션별 스타일을 담고 있는 base_new.html, base_sports.html 등의 템플릿 생성
       - 1단계  템플릿 상속
    3. 개별 페이지에 대한 템플릿 생성
       - 2단계 템플릿 상속

## Form

- 장고에서 제공하는 기능 중 하나

  사용자 입력을 받기 위해 사용되는 텍스트박스, 드롭다운받스와 같은 form을 html에 렌더링하기 위한 것

- form project 생성

- form/forms.py

  ```
  from django import forms
  
  class NameForm(forms.Form):
          your_name = forms.CharField(label='Your name', max_length=100)
  ```

- form/view.py

  ```
  from django.shortcuts import render
  from django.http import HttpResponseRedirect
  
  from forms import NameForm
  
  def get_name(request):
  	# post 방식인지 get 방식인지
      if request.method == 'POST':
          form = NameForm(request.POST)
          # 유효성 검사
          if form.is_valid():
              new_name = form.cleaned_date['name']
          return HttpResponseRedirect('/thanks/')
  
      else:
          form = NameForm()
          return render(request, 'name.html', {'form':form})
  ```

- form/templates.form/name.html

  ```
  <form action="/your-name/" method ='post'>
      {% csrf_token %}
      {{ form }}
      <input type='submit' value="Submit" />
  </form>
  ```

## 로그 남기기

- setting.py

  다음 코드 추가

  ```
  LOGGING = {
      'version' : 1
      'disable_exiting_loggers' : False,
      'handlers' : {
          'console' : {
              'class' : 'logging.StreamHandler',
          }
      }
      'loggers' : {
          'mylogger' : {
              'handlers' : ['console'],
              'level' : 'INFO'
          }
      }
  }
  ```

  view.py

  다음 식으로 로거 호출

  ```
  import logging
  
  logger = logging.getLoger('mylogger')
  
  def my_view(request, arg1, arg):
      if bad_mojo:
          logger.error('Something went wrong!')
  ```


















## 프로젝트 개발 순서

1. setting - 개발 환경 세팅

2. model - 데이터베이스 테이블 생성

   admin - 테이블 register

3. url - url 생성

4. view - view 생성
5. html  생성

























​                                                                                                                                                                                                                                                                                                                                                                            