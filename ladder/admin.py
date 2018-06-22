from django.contrib import admin
from .models import Tags,User,Ladder,Unit,Link,LearningStatus


class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','icon','profile','password')


class LadderAdmin(admin.ModelAdmin):
    list_display = ('id','title','creater','is_public','get_unit','get_recommended_next_ladder','get_recommended_prev_ladder','count_finish_number','count_learning_number')


class UnitAdmin(admin.ModelAdmin):
    list_display = ('title','index','ladder','url')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('latter','prior','user')

admin.site.register(Tags)
admin.site.register(User,UserAdmin)
admin.site.register(Ladder,LadderAdmin)
admin.site.register(Unit,UnitAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(LearningStatus)
