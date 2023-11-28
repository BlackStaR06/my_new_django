from django.contrib import admin
from django.urls import path, include
from . import views, user_login
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('base/', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('home/', views.HOME, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('package/', views.PACKAGE, name='package'),
    path('users/', views.USERS, name='users'),
    path('blog/', views.BLOG, name='blog'),
    path('contact/', views.CONTACT, name='contact'),
    path('profile/', user_login.PROFILE, name='profile'),
    path('edit/', user_login.EDIT, name='edit'),
    path('delete-user/<str:user_id>/', user_login.DELETE, name='delete'),
    path('logout/', user_login.LOGOUT, name='logout'),
    path('login/', user_login.LOGIN, name='login'),
    path('register/', user_login.REGISTER, name='register'),
    # admin
    path('director/', views.DIRECTOR, name='director'),
    path('student_add/', user_login.STUDENT_ADD, name='student_add'),
    path('student_view/', user_login.STUDENT_VIEW, name='student_view'),
    path('student_edit/<str:id>', user_login.STUDENT_EDIT, name='student_edit'),
    path('student_update/', user_login.STUDENT_UPDATE, name='student_update'),
    path('student-delete/<str:student_id>/', user_login.STUDENT_DELETE, name='student_delete'),
    # course
    path('course_add/', user_login.COURSE_ADD, name='course_add'),
    path('course_view/', user_login.COURSE_VIEW, name='course_view'),
    path('course_edit/<str:id>', user_login.COURSE_EDIT, name='course_edit'),
    path('course_update/', user_login.COURSE_UPDATE, name='course_update'),
    path('course-delete/<str:course_id>/', user_login.COURSE_DELETE, name='course_delete'),
    # session
    path('session_add/', user_login.SESSION_ADD, name='session_add'),
    path('session_view/', user_login.SESSION_VIEW, name='session_view'),
    path('session_edit/<str:id>', user_login.SESSION_EDIT, name='session_edit'),
    path('session_update/', user_login.SESSION_UPDATE, name='session_update'),
    path('session-delete/<str:id>/', user_login.SESSION_DELETE, name='session_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
