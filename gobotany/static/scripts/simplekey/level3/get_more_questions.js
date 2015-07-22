define([
    'bridge/jquery',
    'bridge/underscore',
    'simplekey/Filter',
    'simplekey/animation',
    'simplekey/resources'
], function(
    $, _, Filter, animation, resources
) {
    exports = {};

    var characters;             // raw data from the API
    var filter_controller;      // filters active on the page

    var $p;                     // paragraph around button
    var $button;                // "Get More Choices" button
    var $ul = null;             // <ul> of character groups

    exports.install_handlers = function(args) {
        filter_controller = args.filter_controller;

        resources.pile_set(args.pile_slug).done(function(data) {
            characters = data;
            compute_coverage_lists();

            $p = $('#question-nav .get-more');
            $button = $p.find('.get-choices');

            $button.on('click', toggle_group_list);
            $p.on('mouseenter', 'li', display_group_of_characters);
            $p.on('click', 'li[data-character]', add_filter);

            sort_remaining_characters();
        });
    };

    /* Figure out the full list of taxa covered by each character. */

    var compute_coverage_lists = function() {
        for (var i = 0; i < characters.length; i++) {
            var character = characters[i];
            var values = character.values;
            character.taxon_ids_covered = _.intersection(values);
        }
    };

    var sort_remaining_characters = function() {
        return _.chain(characters)
            .filter(not_already_displayed)
            .sortBy('ease')
            .sortBy(demote_lone_choices)
            .sortBy('group_name')
            .value();
    };

    var not_already_displayed = function(character) {
        return ! _.has(filter_controller.filtermap, character.slug);
    };

    var demote_lone_choices = function(character) {
        var useful_values = _.filter(character.values, function(taxon_ids) {
            return _.intersection(taxon_ids, filter_controller.taxa).length;
        });
        return Math.max(useful_values.length, 2);
    };

    /* API routines. */

    var toggle_group_list = function(event) {

        if (! $button.is(event.target))
            return;

        if ($ul === null) {
            var remaining_characters = sort_remaining_characters();
            var group_name = null;
            var $group_ul;

            $ul = $('<ul>').addClass('get-more-questions-menu');
            $ul.appendTo('.get-more');

            _.each(remaining_characters, function(character) {
                if (character.group_name != group_name) {
                    group_name = character.group_name;
                    $group_ul = $('<ul>').appendTo(
                        $('<li>').text(group_name + ' ▸').appendTo($ul));
                }
                var debug_info = '(ease ' + character.ease + ') ';
                $group_ul.append($('<li>', {
                    'text': debug_info + character.name,
                    // 'text': character.name,
                    'data-character': character.slug
                }));
            });
        } else {
            $ul.remove();
            $ul = null;
        }
    };

    var display_group_of_characters = function() {
        var $ul_beneath = $(this).find('ul');
        if ($ul_beneath.length) {
            $p.find('ul ul').hide();
            $ul_beneath.show();
        }
    };

    var add_filter = function() {
        var slug = $(this).attr('data-character');
        $(this).removeAttr('data-character');

        var info = _.find(characters, function(character) {
            return character.slug === slug;
        });

        info.friendly_name = info.name;  /* TODO: fix the mismatch? */
        info.short_name = info.slug;     /* TODO: fix the mismatch? */

        var filter = Filter.create({
            slug: info.slug,
            value_type: info.type,
            info: info
        });

        /* TODO: the following dance is also in results.js. */

        filter_controller.add(filter);

        Ember.run.next(function() {
            var $filters = $('#sidebar ul li');
            var $new = $filters.eq(-1);
            animation.bright_change($new);  /* why doesn't this work? */
            // Scroll to the bottom of the list to reveal the new filter. 
            var $filter_list = $('.scroll');
            var scroll_position =
                $filter_list[0].scrollHeight - $filter_list.height();
            $filter_list.animate(
                {scrollTop: scroll_position + 'px'},
                'fast',
                'swing'
            );
        });

        // With a filter having been chosen, dismiss the menu.
        $ul = $('.get-more-questions-menu')[0];
        $ul.remove();
        $ul = null;
    };

    return exports;
});
