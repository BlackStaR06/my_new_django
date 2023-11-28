from django.urls import path
from .views import CustomUserView, StudentView, CourseView, SessionTimeView, CustomUserViewDetails, StudentViewDetails, CourseViewDetails, SessionTimeViewDetails
urlpatterns = [
    path('user/', CustomUserView.as_view(), name='user_api'),
    path('student/', StudentView.as_view(), name='student_api'),
    path('course/', CourseView.as_view(), name='course_api'),
    path('session/', SessionTimeView.as_view(), name='session_api'),
    path('user/<int:pk>', CustomUserViewDetails.as_view(), name='user_edit-api'),
    path('student/<int:pk>', StudentViewDetails.as_view(), name='student_edit-api'),
    path('course/<int:pk>', CourseViewDetails.as_view(), name='course_edit-api'),
    path('session/<int:pk>', SessionTimeViewDetails.as_view(), name='session_edit-api')
]
