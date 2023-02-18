from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'studyonline'
urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),

 ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






