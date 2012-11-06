# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.vary import vary_on_headers

from gobotany.core.models import ContentImage, Pile, PileGroup
from gobotany.core.partner import which_partner
from gobotany.simplekey.groups_order import ordered_pilegroups, ordered_piles
from gobotany.simplekey.models import (GroupsListPage,
                                       SubgroupResultsPage,
                                       SubgroupsListPage)
from gobotany.taxa.views import _images_with_copyright_holders

# Character short names common to all piles (but no suffix)
COMMON_CHARACTERS = ['habitat', 'habitat_general', 'state_distribution']

#

def add_query_string(request, url):
    full = request.get_full_path()
    i = full.find('?')
    return url if (i == -1) else url + full[i:]

#

def per_partner_template(request, template_path):
    partner = which_partner(request)
    if partner and partner.short_name != 'gobotany':
        return '{0}/{1}'.format(partner.short_name, template_path)
    else:
        return template_path

#

def get_simple_url(key, pilegroup, pile=None):
    if pile is None:
        return reverse('gobotany.simplekey.views.level2',
                       kwargs={'key': key,
                               'pilegroup_slug': pilegroup.slug})
    else:
        return reverse('gobotany.simplekey.views.level3',
                       kwargs={'key': key,
                               'pilegroup_slug': pilegroup.slug,
                               'pile_slug': pile.slug})


def _partner_short_name(partner):
    short_name = None
    if partner:
        short_name = partner.short_name
    return short_name

@vary_on_headers('Host')
@cache_control(max_age=60 * 60)
@cache_page(60 * 60)
def level1(request, key):
    partner = which_partner(request)
    short_name = _partner_short_name(partner)
    groups_list_page = GroupsListPage.objects.get()

    pilegroups = []
    for pilegroup in ordered_pilegroups():
        images = _images_with_copyright_holders(
            ContentImage.objects.filter(
                pilegroupimage__pile_group=pilegroup)
            .select_related('image_type'))
        pilegroups.append((pilegroup, images, get_simple_url(key, pilegroup)))

    return render_to_response('simplekey/simple.html', {
            'partner_site': short_name,
            'groups_list_page': groups_list_page,
            'key': key,
            'pilegroups': pilegroups
            }, context_instance=RequestContext(request))

@vary_on_headers('Host')
@cache_control(max_age=60 * 60)
@cache_page(60 * 60)
def level2(request, key, pilegroup_slug):
    pilegroup = get_object_or_404(PileGroup, slug=pilegroup_slug)

    partner = which_partner(request)
    short_name = _partner_short_name(partner)
    subgroups_list_page = SubgroupsListPage.objects.get(group=pilegroup)

    piles = []
    for pile in ordered_piles(pilegroup):
        images = _images_with_copyright_holders(
            ContentImage.objects.filter(pileimage__pile=pile)
            .select_related('image_type'))
        piles.append((pile, images, get_simple_url(key, pilegroup, pile)))

    # For Issue #254, Full Key, mock up a possible solution
    if key.lower() == 'full':
        piles.append(piles[1])  # Duplicate the last pile

    return render_to_response('simplekey/pilegroup.html', {
            'partner_site': short_name,
            'subgroups_list_page': subgroups_list_page,
            'key': key,
            'pilegroup': pilegroup,
            'piles': piles
            }, context_instance=RequestContext(request))

def level3(request, key, pilegroup_slug, pile_slug):
    pile = get_object_or_404(Pile, slug=pile_slug)
    if pile.pilegroup.slug != pilegroup_slug:
        raise Http404

    partner = which_partner(request)
    short_name = _partner_short_name(partner)
    subgroup_results_page = SubgroupResultsPage.objects.get(subgroup=pile)

    return render_to_response('simplekey/results.html', {
           'key': key,
           'partner_site': short_name,
           'subgroup_results_page': subgroup_results_page,
           'pilegroup': pile.pilegroup,
           'pile': pile,
           }, context_instance=RequestContext(request))


# We have moved the 2nd and 3rd level Simple Key pages beneath /simple/
# so we need these redirections in place for a while.

def redirect_pilegroup_to_simple(request, pilegroup_slug):
    get_object_or_404(PileGroup, slug=pilegroup_slug)
    return redirect('/simple' + request.path, permanent=True)

def redirect_pile_to_simple(request, pilegroup_slug, pile_slug):
    pile = get_object_or_404(Pile, slug=pile_slug)
    if pile.pilegroup.slug != pilegroup_slug:
        raise Http404
    return redirect('/simple' + request.path, permanent=True)
