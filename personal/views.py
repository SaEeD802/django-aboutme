from django.shortcuts import render
from resume.models import Project
from contactus.models import Footer,Message


def home(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')
        Message.objects.create(fname=fname, email=email, sub=sub, body=body)
    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    
    context = {
        'projects': projects,
        'footer': footer
    }
    return render(request, 'index.html', context)