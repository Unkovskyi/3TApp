from django.urls import path

from . import views

app_name = 'currency_exchange'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('tasks/list', views.TasksList.as_view(), name='tasks-list'),
    path('projects/list', views.ProjectsList.as_view(), name='project-list'),
    path('provider/list/', views.ProviderList.as_view(), name='provider-list'),
    path('provider/<str:provider_id>/load/',views.admin_run_load_data, name='admin-provider-load')
]
