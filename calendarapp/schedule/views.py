from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Course, ScheduledCourse, Classroom, Ogretmen
import json

def home(request):
    try:
        courses = Course.objects.all()
        scheduled_courses = ScheduledCourse.objects.all()
        classrooms = Classroom.objects.all()
        ogretmenler = Ogretmen.objects.all()
        print("Sınıflar:", list(classrooms))  # Debug için
        return render(request, 'schedule/home.html', {
            'courses': courses,
            'scheduled_courses': scheduled_courses,
            'classrooms': classrooms,
            'ogretmenler': ogretmenler
        })
    except Exception as e:
        print("Hata:", str(e))  # Debug için
        return render(request, 'schedule/home.html', {
            'courses': [],
            'scheduled_courses': [],
            'classrooms': [],
            'ogretmenler': []
        })

@csrf_exempt
def upload_excel(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        print("excel geldi")
        excel_file = request.FILES['excel_file']
        try:
            # Excel'i oku ve ilk satırı atlar (başlıklar karışık olduğu için)
            df = pd.read_excel(excel_file, skiprows=1)
            print("Sütunlar:", df.columns.tolist())
            print("İlk satır:", df.iloc[0].tolist())
            
            Course.objects.all().delete()  # Clear existing courses
            
            for index, row in df.iterrows():
                try:
                    # Sütun indekslerini kullanarak verileri al
                    code = str(row.iloc[2])  # 3. sütun (0'dan başlayarak)
                    name = str(row.iloc[3])  # 4. sütun
                    instructor = str(row.iloc[4])  # 5. sütun
                    total = row.iloc[7]  # 8. sütun
                    duration = row.iloc[5]  # 6. sütun (Süre sütunu)
                    
                    if pd.notna(code) and pd.notna(name):  # Boş satırları atla
                        Course.objects.create(
                            code=code,
                            name=name,
                            instructor=instructor,
                            total_students=int(total) if pd.notna(total) else 0,
                            duration=int(duration) if pd.notna(duration) else 60  # Varsayılan 60 dakika
                        )
                        print(f"Ders eklendi: {code} - {name} - Süre: {duration}")
                except Exception as e:
                    print(f"Satır işlenirken hata: {e}")
                    print(f"Satır verisi: {row.tolist()}")
                    continue
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'No file uploaded'})

@csrf_exempt
def save_schedule(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ScheduledCourse.objects.all().delete()  # Clear existing schedule
            
            for item in data:
                course = Course.objects.get(id=item['course_id'])
                ScheduledCourse.objects.create(
                    course=course,
                    day=item['day'],
                    start_time=item['start_time'],
                    end_time=item['end_time']
                )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}) 