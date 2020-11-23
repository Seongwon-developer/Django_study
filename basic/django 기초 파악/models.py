# Model - 데이터베이스 정의

from django.db import models

# Person 클래스 : SQL 명령을 사용하여 다음과 같은 장고 내부에 데이터베이스 테이블 생성
# CREATE TABLE myapp_person(
#   "id" serial NOT NULL PRIMARY KEY,
#   "first_name" varchar(30) NOT NULL,
#   "last_name" varchar(30) NOT NULL
# );
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)