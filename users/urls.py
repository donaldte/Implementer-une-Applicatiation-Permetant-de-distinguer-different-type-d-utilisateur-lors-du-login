from django.urls import path
from users.views import home, register, doctor, infimiere, patient

urlpatterns = [
    path('', home, name="home"),
    path('register', register, name='register'),
    path('doctor', doctor, name='doctor'),
    path('infimiere', infimiere, name='infimiere'),
    path('patient', patient, name='patient'),
]
