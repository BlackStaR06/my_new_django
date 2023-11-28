from rest_framework import serializers
from app.models import CustomUser, Student, SessionTime, Course


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'profile_pic')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('course_id', )


class SessionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionTime
        fields = ('session_start', 'session_end')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'created_ad', 'updated_ad')
