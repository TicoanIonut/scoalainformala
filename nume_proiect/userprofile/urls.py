from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
	path('new_account/', views.CreateNewAccount.as_view(), name= 'utilizator_nou'),
	path('start_timesheet/', views.new_timesheet, name='start_pontaj'),
	path('stop_timesheet/', views.stop_timesheet, name='stop_pontaj'),
]
