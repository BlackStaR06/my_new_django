from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import CustomUser, Student, SessionTime, Course
from .serializers import CustomUserSerializer, StudentSerializer, SessionTimeSerializer, CourseSerializer


class CustomUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SessionTimeView(ListCreateAPIView):
    queryset = SessionTime.objects.all()
    serializer_class = SessionTimeSerializer


class CourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CustomUserViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class StudentViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SessionTimeViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = SessionTime.objects.all()
    serializer_class = SessionTimeSerializer


class CourseViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
