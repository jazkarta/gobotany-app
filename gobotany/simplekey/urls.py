from django.conf.urls import patterns, url

from gobotany.simplekey import views

urlpatterns = patterns(
    '',

    # Levels 1 (groups), 2 (subgroups), and 3 (filterable results) pages

    url('^(?P<key>simple|full)/$', views.level1, name='level1'),
    url('^(?P<key>simple|full)/(?P<pilegroup_slug>[^/]*)/$',
        views.level2, name='level2'),
    url('^(?P<key>simple|full)/(?P<pilegroup_slug>[^/]*)/(?P<pile_slug>[^/]*)/$',
        views.level3, name='level3'),

    # Old URLs at which the Simple Key 2nd and 3rd-level pages once lived.

    url('^(?P<pilegroup_slug>[^/]*)/$',
        views.redirect_pilegroup_to_simple),
    url('^(?P<pilegroup_slug>[^/]*)/(?P<pile_slug>[^/]*)/$',
        views.redirect_pile_to_simple),
    )
