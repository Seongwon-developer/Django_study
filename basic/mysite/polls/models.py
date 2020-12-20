import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')           # 생성 시간 저장
    
    def __str__(self):          ## __str__ 함수 : shell을 편하게 사용하기 위해서 사용
        return self.question_text
    
    def was_published_recently(self):
        # system 기준 시간과 django 기준 시간의 차이 비교 true false return
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

# Create your models here.
