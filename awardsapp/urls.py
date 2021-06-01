from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.home_projects, name='homePage'),
    path('search/', views.search_projects, name='search_projects'),
    re_path('image(\d+)', views.project, name='project'),
    path('users/', views.user_list, name='user_list'),
    path('new/image', views.new_image, name='new_image'),
    path('new/project', views.new_project, name='new_project'),
    path('edit/profile', views.edit_profile, name='edit_profile'),
    re_path('profile/(?P<username>[0-9]+)',
        views.individual_profile_page, name='individual_profile_page'),
    path('ajax/newsletter/', views.newsletter, name='newsletter'),
    path('api/project/', views.ProjectList.as_view()),
    re_path('api/project/project-id/(?P<pk>[0-9]+)/',
        views.ProjectDescription.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    re_path('api/profile/profile-id/(?P<pk>[0-9]+)/',
        views.ProfileDescription.as_view()),
    # ex: /
    path('', views.review_list, name='review_list'),
    # ex: /review/5/
    re_path('review/(?P<review_id>[0-9]+)/',
        views.review_detail, name='review_detail'),
    # ex: /project/
    path('project', views.project_list, name='project_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)