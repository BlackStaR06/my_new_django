from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from app.models import CustomUser, Course, SessionTime, Student
from app.EmailBackend import EmailBackend


def REGISTER(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        profile_pic = request.FILES.get('profile_pic')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This email already exists')
            return redirect('register')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username already exists')
            return redirect('register')
        user = CustomUser(
            email=email,
            username=username,
            user_type=user_type,
            profile_pic=profile_pic
        )
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, 'registration/register.html')


def LOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackend.authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('director')
            elif user_type == '2':
                return HttpResponse('Welcome teacher')
            else:
                return redirect('profile')
        else:
            messages.warning(request, 'Login or password is incorrect')
            return redirect('login')
    return render(request, 'registration/login.html')


def LOGOUT(request):
    logout(request)
    return redirect('login')


def PROFILE(request):
    return render(request, 'Main/profile.html')


def EDIT(request):
    return render(request, 'Main/edit.html')


def UPDATEPROFILE(request):
    if request.method == 'POST':
        u_email = request.POST.get('email')
        u_username = request.POST.get('username')
        u_first_name = request.POST.get('first_name')
        u_last_name = request.POST.get('last_name')
        try:
            user = CustomUser.objects.get(id=request.user.id)
            user.email = u_email
            user.username = u_username
            user.first_name = u_first_name
            user.last_name = u_last_name
            user.save()
            messages.success(request, 'Your information has been changed')
            return redirect('profile')
        except:
            messages.error(request, 'Something went wrong! Try again')
            return redirect('edit')
    return redirect('profile')


def DELETE(request, user_id):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return redirect('users')

# admin


def STUDENT_ADD(request):
    course = Course.objects.all()
    session = SessionTime.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_time = request.POST.get('session_time')
        address = request.POST.get('address')
        print(first_name, last_name, username, email, password, profile_pic, gender, course_id, session_time, address)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This email already exists')
            return redirect('student_add')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username already exists')
            return redirect('student_add')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course_id)
            session_time1 = SessionTime.objects.get(id=session_time)
            student = Student(
                admin=user,
                address=address,
                course_id=course,
                session_id=session_time1,
                gender=gender
            )
            student.save()
            messages.success(request, f"{email} has been registered")
            return redirect('student_view')
    context = {
        'course': course,
        'session': session
    }
    return render(request, 'admin/student_add.html', context=context)


def STUDENT_VIEW(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'admin/student_view.html', context=context)


def STUDENT_EDIT(request, id):
    student_id = Student.objects.get(id=id)
    course = Course.objects.all()
    session = SessionTime.objects.all()
    context = {
        'student_id': student_id,
        'course': course,
        'session': session
    }
    return render(request, 'admin/student_edit.html', context=context)


def STUDENT_UPDATE(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_time = request.POST.get('session_time')
        address = request.POST.get('address')
        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        if password is not None and password is not '':
            user.set_password(password)
        if profile_pic is not None and profile_pic is not '':
            user.profile_pic = profile_pic
        user.save()
        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender
        student.course_id = Course.objects.get(id=course_id)
        student.address = address
        student.gender = gender
        course = Course.objects.get(id=course_id)
        student.course_id = course
        session = SessionTime.objects.get(id=session_time)
        student.session_id = session
        student.save()
        messages.success(request, 'Updated')
        return redirect('student_view')
    return redirect('student_edit')


def STUDENT_DELETE(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    messages.warning(request, 'Deleted')
    return redirect('student_view')

# course


def COURSE_ADD(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        course = Course(
            name=name
        )
        course.save()
        messages.success(request, 'New course has been added')
        return redirect('course_view')
    return render(request, 'admin/course_add.html')


def COURSE_VIEW(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'admin/course_view.html', context=context)


def COURSE_DELETE(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    messages.warning(request, 'Deleted')
    return redirect('course_view')


def COURSE_EDIT(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, 'admin/course_edit.html', context=context)


def COURSE_UPDATE(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        course = Course.objects.get(id=id)
        course.name = name
        course.save()
        messages.success(request, 'Updated')
        return redirect('course_view')
    return redirect('course_edit')

# session


def SESSION_ADD(request):
    if request.method == 'POST':
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = SessionTime(
            session_start=session_start,
            session_end=session_end
        )
        session.save()
        messages.success(request, 'New session has been added')
        return redirect('session_view')
    return render(request, 'admin/session_add.html')


def SESSION_VIEW(request):
    session = SessionTime.objects.all()
    context = {
        'session': session
    }
    return render(request, 'admin/session_view.html', context=context)


def SESSION_EDIT(request, id):
    session = SessionTime.objects.get(id=id)
    context = {
        'session': session
    }
    return render(request, 'admin/session_edit.html', context=context)


def SESSION_UPDATE(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        session = SessionTime.objects.get(id=id)
        session.session_start = session_start
        session.session_end = session_end
        session.save()
        messages.success(request, 'Updated')
        return redirect('session_view')
    return redirect('session_edit')


def SESSION_DELETE(request, id):
    session = SessionTime.objects.get(id=id)
    session.delete()
    messages.warning(request, 'Deleted')
    return redirect('session_view')
