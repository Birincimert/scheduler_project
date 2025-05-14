from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    professor = models.CharField(max_length=100, blank=True)
    duration = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.lesson.name} - {self.day} ({self.start_time} - {self.end_time})"
