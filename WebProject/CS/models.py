from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    # slug 컬럼은 제목의 별칭 , unique 옵션을 추가해 특정 포스트를 검색시 기본 키 대신에 사용, allow_unicode 옵션을 추가하면 한글
    # 한글 처리 가능 help_text는 해당 컬럼을 설명해주는 문구로 폼 화면에 나타납니다. admin 사이트에서 확인 가능
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

# 필드 속성 외에 필요한 파라미터가 있으면 ,Meta 내부 클래스로 정의한다.

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        # 데이터베이스에 저장되는 테이블의 이름을 지정 생략하면 디폴트는 '앱명_모델클래스명'을 테이블명으로 지정 ex) CS_post
        # db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CS:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post,self).save(*args, **kwargs)
