from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def patient_page(request):
    return render(request, 'patient.html')

def dentist_page(request):
    return render(request, 'dentist.html')

def receptionist_page(request):
    return render(request, 'receptionist.html')