from django.shortcuts import render
from .models import Resume
from .utils import extract_text
from .ai import analyze_resume
from .models import Resume

def home(request):

    result = None

    if request.method == 'POST':

        role = request.POST.get('role')
        resume_file = request.FILES['resume']
        resume_obj = Resume.objects.create(
    resume=resume_file
)

        text = extract_text(resume_file)

        result = analyze_resume(text, role)

    return render(request, 'home.html', {'result': result})