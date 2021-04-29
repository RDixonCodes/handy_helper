from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create', views.create_user),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/hello', views.dashboard),
    path('user/job', views.job),
    path('new/job', views.create_job),
    path('give/<int:job_id>/job', views.move_job),
    path('add/<int:job_id>/job', views.add_job),
    path('job/<int:job_id>/edit', views.edit_job),
    path('edit/<int:job_id>/job', views.update_job),
    path('job/<int:job_id>/view', views.view_job),
    path('remove/<int:job_id>', views.delete_job)
]