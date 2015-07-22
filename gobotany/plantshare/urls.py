from django.conf.urls import patterns, url, include

from gobotany.plantshare import views

urlpatterns = patterns(
    '',

    # PlantShare main page
    url(r'^$', views.plantshare_view, name='ps-main'),

    # Facebook login
    url(r'^facebook_connect/', include('facebook_connect.urls')),
    # Normal registration login
    url(r'^accounts/', include('gobotany.plantshare.backends.default.urls')),

    # Terms of Agreement
    url(r'^terms-of-agreement/accept/$', views.terms_of_agreement_accept_view,
        name='ps-terms-of-agreement-accept'),
    url(r'^terms-of-agreement/$', views.terms_of_agreement_view,
        name='ps-terms-of-agreement'),

    # Post a (new) Sighting form
    url(r'^sightings/new/$', views.new_sighting_view, name='ps-new-sighting'),
    url(r'^sightings/new/done/$', views.new_sighting_done_view,
        name='ps-new-sighting-done'),

    # Sightings Locator
    url(r'^sightings/locator/$', views.sightings_locator_view,
        name='ps-sightings-locator'),

    # Manage Your Sightings
    url(r'^sightings/manage/$', views.manage_sightings_view,
        name='ps-manage-sightings'),
    url(r'^sightings/(?P<sighting_id>[0-9]+)/edit/$',
        views.edit_sighting_view, name='ps-edit-sighting'),
    url(r'^sightings/edit/done/$', views.edit_sighting_done_view,
        name='ps-edit-sighting-done'),
    url(r'^sightings/(?P<sighting_id>[0-9]+)/delete/$',
        views.delete_sighting_view, name='ps-delete-sighting'),
    url(r'^sightings/(?P<sighting_id>[0-9]+)/$', views.sighting_view,
        name='ps-sighting'),

    # Recent Sightings, and sightings by year
    url(r'^sightings/$', views.sightings_view, name='ps-sightings'),
    url(r'^sightings/year-(?P<year>[0-9]{4})/$',
        views.sightings_by_year_view, name='ps-sightings-by-year'),

    # Ask the Botanist
    url(r'^questions/$', views.questions_view, name='ps-questions'),
    url(r'^questions/new/done/$', views.new_question_done_view,
        name='ps-new-question-done'),
    url(r'^questions/all/(?P<year>[0-9]{4})/$',
        views.all_questions_by_year_view,
        name='ps-all-questions-by-year'),
    url(r'^questions/all/$', views.all_questions_by_year_view,
        name='ps-all-questions'),

    # Checklists
    url(r'^checklists/$', views.checklist_index_view, name='ps-checklists'),
    url(r'^checklists/new/$', views.new_checklist_view,
        name='ps-checklist-new'),
    url(r'^checklists/delete/$', views.delete_checklists_view,
        name='ps-checklists-delete'),
    url(r'^checklists/(?P<checklist_id>[0-9]+)/$', views.checklist_view,
        name='ps-checklist'),
    url(r'^checklists/(?P<checklist_id>[0-9]+)/export/$',
        views.export_checklist_view, name='ps-checklist-export'),
    url(r'^checklists/(?P<checklist_id>[0-9]+)/edit/$',
        views.edit_checklist_view, name='ps-checklist-edit'),
    # dialog for AJAX-based delete of single checklist
    url(r'^checklists/(?P<checklist_id>[0-9]+)/delete/$',
        views.delete_checklist_view, name='ps-checklist-delete'),

    # Find People
    url(r'^people/$', views.find_people_view, name='ps-find-people'),
    url(r'^people/(?P<username>[A-Za-z0-9_@+-.]+)/$',
        views.find_people_profile_view, name='ps-find-people-profile'),

    # Your Profile page
    url(r'^profile/$', views.your_profile_view, name='ps-your-profile'),

    # Staff-Only area urls
    url(r'^staff/images$', views.screen_images, name='ps-screen-images'),

    # AJAX urls
    url(r'^api/edit-profile$', views.ajax_profile_edit,
        name='ps-ajax-profile-edit'),
    url(r'^api/image-upload$', views.ajax_image_upload,
        name='ps-ajax-image-upload'),
    url(r'^api/image-reject/(?P<image_id>[0-9]+)$', views.ajax_image_reject,
        name='ps-ajax-image-reject'),
    url(r'^api/sightings/$', views.ajax_sightings, name='ps-ajax-sightings'),
    url(r'^api/people-suggestions/$', views.ajax_people_suggestions,
        name='ps-ajax-people-suggestions'),
    url(r'^api/restrictions/$', views.ajax_restrictions,
        name='ps-ajax-restrictions'),
    )
