from django.shortcuts import render

# Create your views here.
def student_dashboard(request):
    return render(request, 'students/dashboard.html')