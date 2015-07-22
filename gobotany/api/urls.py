from django.conf import settings
from django.conf.urls import patterns, url
from django.contrib import admin
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import RedirectView

from gobotany.api import handlers, views
from piston.resource import Resource

admin.autodiscover()

handler500 = 'django.views.defaults.server_error'

def allow_cross_site_access(f):
    """The Dichotomous Key needs to fetch lists of images for display.

    Someday we might consider restricting the '*' down to a list of the
    domains where the DK and its test and dev versions are actually
    running; but for now we allow it to run anywhere.

    """
    def add_cross_site_header(*args, **kw):
        httpresponse = f(*args, **kw)
        httpresponse['Access-Control-Allow-Origin'] = '*'
        return httpresponse
    return add_cross_site_header

urlpatterns = patterns(
    '',

    url(r'^taxa/(?P<scientific_name>[^/]+)/$', allow_cross_site_access(
            Resource(handler=handlers.TaxonQueryHandler)), name='api-taxa'),
    url(r'^taxa/$',
        Resource(handler=handlers.TaxonQueryHandler), name='api-taxa-list'),

    url(r'^taxa-count/$',
        Resource(handler=handlers.TaxonCountHandler), name='api-taxa-count'),

    url(r'^taxon-image/$',
        Resource(handler=handlers.TaxonImageHandler), name='api-taxon-image'),

    url(r'^characters/$',
        Resource(handler=handlers.CharactersHandler)),
    url(r'^characters/(?P<character_short_name>[^/]+)/$',
        Resource(handler=handlers.CharacterHandler)),

    url(r'^piles/$',
        Resource(handler=handlers.PileListingHandler), name='api-pile-list'),


    # Redirects for the split Remaining Non-Monocots piles, so that the
    # Get More Questions feature works for them
    url(r'^piles/(?:non-)?alternate-remaining-non-monocots/characters/$',
        RedirectView.as_view(
            url='/api/piles/remaining-non-monocots/characters/',
            query_string=True
            )),
    url(r'^piles/(?:non-)?alternate-remaining-non-monocots/questions/$',
        RedirectView.as_view(
            url='/api/piles/remaining-non-monocots/questions/',
            query_string=True
            )),
    url(r'^piles/(?:non-)?alternate-remaining-non-monocots/$',
        RedirectView.as_view(
            url='/api/piles/remaining-non-monocots/')),


    url(r'^piles/(?P<pile_slug>[^/]+)/characters/$',
        'gobotany.api.views.piles_characters',
        name='api-character-list'),

    url(r'^piles/(?P<pile_slug>[^/]+)/questions/$',
        'gobotany.api.views.questions', name='api-questions'),

    url(r'^piles/(?P<slug>[^/]+)/?$',
        Resource(handler=handlers.PileHandler), name='api-pile'),

    url(r'^piles/(?P<pile_slug>[^/]+)/(?P<character_short_name>[^/]+)/$',
        Resource(handler=handlers.CharacterValuesHandler),
        name='api-character-values'),

    url(r'^pilegroups/$',
        Resource(handler=handlers.PileGroupListingHandler),
        name='api-pilegroup-list'),
    url(r'^pilegroups/(?P<slug>[^/]+)/$',
        Resource(handler=handlers.PileGroupHandler), name='api-pilegroup'),

    # Plant distribution maps
    url(r'^maps/(?P<genus>[^/-]+)-(?P<epithet>[^/]+)'
         '-ne-distribution-map(\.svg|/)?$',
        views.new_england_distribution_map, name='ne-distribution-map'),
    url(r'^maps/(?P<genus>[^/-]+)-(?P<epithet>[^/]+)'
         '-na-distribution-map(\.svg|/)?$',
        views.north_american_distribution_map, name='na-distribution-map'),

    url(r'^$', 'nonexistent', name='api-base'),  # helps compute the base URL
    )

# We only use caching if memcached itself is configured; otherwise, we
# assume that the developer does not really intend caching to take
# place.

if 'memcache' in settings.CACHES['default']['BACKEND']:
    one_hour = 60 * 60
    browsercache = cache_control(maxage=one_hour)
    memcache = cache_page(one_hour)
    both = lambda view: browsercache(memcache(view))
else:
    browsercache = lambda view: view
    memcache = lambda view: view
    both = lambda view: view

urlpatterns += patterns(
    'gobotany.api.views',
    url(r'^glossaryblob/$', both(views.glossary_blob)),
    url(r'^hierarchy/$', both(views.hierarchy)),
    url(r'^dkey-images/([-\w\d]+)/$', both(views.dkey_images)),
    url(r'^families/([\w]+)/$', both(views.family)),
    url(r'^genera/([\w]+)/$', both(views.genus)),
    url(r'^species/([\w-]+)/$', browsercache(views.species)),
    url(r'^vectors/character/([\w()-]+)/$', both(views.vectors_character)),
    url(r'^vectors/key/([\w-]+)/$', both(views.vectors_key)),
    url(r'^vectors/pile/([\w-]+)/$', both(views.vectors_pile)),

    # Another redirect for the split Remaining Non-Monocots piles, for
    # the feature Get More Questions > Pick Your Own
    url(r'^vectors/pile-set/(?:non-)?alternate-remaining-non-monocots/$',
        RedirectView.as_view(
            url='/api/vectors/pile-set/remaining-non-monocots/')),

    url(r'^vectors/pile-set/([\w-]+)/$', both(views.pile_vector_set)),
    )
