from django.shortcuts import render
from app.models import Course, SessionTime, Student


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    course = Course.objects.all()
    session = SessionTime.objects.all()
    student = Student.objects.all()
    context = {
        'student': student,
        'session': session,
        'course': course
    }
    return render(request, 'Main/home.html', context=context)


def ABOUT(request):
    return render(request, 'Main/about.html')


def PACKAGE(request):
    return render(request, 'Main/packages.html')


def USERS(request):
    return render(request, 'Main/users.html')


def BLOG(request):
    return render(request, 'Main/blog.html')


def CONTACT(request):
    return render(request, 'Main/contact.html')

# admin


def DIRECTOR(request):
    return render(request, 'admin/index.html')
