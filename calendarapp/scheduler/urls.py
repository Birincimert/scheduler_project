from django.urls import path
from .views import home, upload_excel  # Görünümlerimizi içe aktardık

app_name = 'scheduler'

urlpatterns = [
    path('', home, name='home'),  # Ana sayfa rotası
    path('upload/', upload_excel, name='upload_excel'),  # Excel yükleme rotası
]
