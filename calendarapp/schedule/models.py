from django.db import models

class Classroom(models.Model):
    sinif_no = models.CharField(max_length=10, unique=True)
    kapasite = models.IntegerField()

    def __str__(self):
        return f"{self.sinif_no} - {self.kapasite} kişilik"

    class Meta:
        verbose_name = "Sınıf"
        verbose_name_plural = "Sınıflar"

class Course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)  # Toplam öğrenci sayısı
    duration = models.IntegerField(default=60)  # Ders süresi (dakika cinsinden)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class ScheduledCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.course.code} - {self.get_day_display()}"

    class Meta:
        ordering = ['day', 'start_time']

class Ogretmen(models.Model):
    ad_soyad = models.CharField(max_length=100)
    kisaltma = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.ad_soyad} ({self.kisaltma})"

    class Meta:
        db_table = 'ogretmenler'
        verbose_name = 'Öğretim Elemanı'
        verbose_name_plural = 'Öğretim Elemanları' 