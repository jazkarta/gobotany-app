/* Sightings Locator component part with an input box and map.
 *
 * Note:
 * The map requires that this be set up at onload, not at jQuery ready. */
define([
    'bridge/jquery',
    'bridge/jquery.cookie',
    'plantshare/sightings_map'
], function ($, x1, SightingsMap) {

    function SightingsLocatorPart(locator_element_css) {
        // Constructor
        
        this.$locator_element = $(locator_element_css);
        this.$plant_name_field = this.$locator_element.find(
            'input[type="text"]').first();
        this.current_plant_name = '';
        var plant_name = $.cookie('last_locator_name');
        // If there is a non-empty plant name string from the user's
        // previous search, restore it to the input box.
        if (plant_name) {
            this.current_plant_name = plant_name;
            this.$plant_name_field.val(this.current_plant_name);
        }

        this.$plant_name_field.on('keyup', function (event) {
            if (event.keyCode !== 13) {   // Enter key
                // Hide the results status message as soon as typing starts.
                var color = $('#sightings-status').css('background-color');
                $('#sightings-status').css('color', color);
            }
        });
    };

    SightingsLocatorPart.prototype.show_sightings = function (plant_name,
                                                              sightings_map) {
        // Store the latest plant name searched, then get the sightings.
        this.current_plant_name = plant_name;
        $.cookie('last_locator_name', this.current_plant_name,
            {path: '/'});
        sightings_map.show_sightings(this.current_plant_name);
    };

    SightingsLocatorPart.prototype.setup = function () {
        // Set up the map and form.

        var map_div = this.$locator_element.find('.map').first();

        // Restore the last map location, zoom level, and sighting
        // viewed, if any.
        var cookie_names = {
            'center': 'last_locator_center',
            'zoom': 'last_locator_zoom',
            'last_viewed': 'last_locator_sighting',
            'last_plant_name': 'last_locatior_name'
        }
        var sightings_map = new SightingsMap(map_div, cookie_names);
        sightings_map.setup();

        // Restore the last plant searched in the Sightings Locator, if any.
        // Otherwise, just show some recent sightings.
        if (this.current_plant_name.length > 0) {
            this.show_sightings(this.current_plant_name, sightings_map);
        }
        else {
            sightings_map.show_sightings();
        }

        this.$locator_element.submit($.proxy(
            function (e) {
                e.preventDefault();  // prevent form submit because using AJAX

                var plant_name = this.$plant_name_field.val();
                if (plant_name !== this.current_plant_name) {
                    this.show_sightings(plant_name, sightings_map);
                }
            }, this)
        );

        // For the full-page Sightings Locator, allow clicking on its
        // sightings gallery images to show their locations on the map.
        $('#species-images a').unbind('click');   // prevent multiple bindings
        $('#species-images a').bind('click', function (event) {
            event.preventDefault();
            var sighting_id = $(this).attr('href').split('/')[3];
            sightings_map.show_sighting(sighting_id, cookie_names);
        });
    };

    // Return the constructor function.
    return SightingsLocatorPart;
});
