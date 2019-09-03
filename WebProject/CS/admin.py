from django.contrib import admin
from CS.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):  # PostAdmin 클래스는 Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스입니다.
    list_display = ('title', 'modify_date')  # Post 객체를 보여줄 때 title과 modify_date를 화면에 출력하라고 지정합니다.
    list_filter = ('modify_date',)   # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정합니다.
    search_fields = ('title', 'content')  # 검색박스를 표시하고, 입력된 단어는 title과 content 컬럼에서 검색하도록 합니다.
    prepopulated_fields = {'slug': ('title',)}  # slug 필드는 title 필드를 사용해 미리 채워지도록 합니다.


admin.site.register(Post, PostAdmin)  # admin.site.register()함수를 사용해 Post와 PostAdmin 클래스를 Admin 사이트에 등록합니다.

