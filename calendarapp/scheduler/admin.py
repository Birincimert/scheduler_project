from django.contrib import admin
from .models import Lesson, Schedule  # Modellerimizi burada kullanıyoruz

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'professor', 'duration')
    search_fields = ('name', 'code', 'professor')
    list_filter = ('professor',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    
    def get_lesson_name(self, obj):
        return obj.lesson.name
    get_lesson_name.short_description = 'Ders Adı'
