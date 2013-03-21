/*
 * Code for special handling of full plant photos.
 */
define([
    'bridge/jquery',
    'util/shadowbox_init'
], function($, shadowbox_init) {

var PhotoHelper = {

    init: function() {
    },

    prepare_to_enlarge: function() {
        // Do a few things before enlarging the photo on the screen.
        // Intended to be called using the Shadowbox onOpen handler.

        var title_element = $('#sb-title-inner').first();

        // Temporarily hide the title element.
        title_element.addClass('hidden');

        // Call a function to do the usual Shadowbox initialization because
        // an existing onOpen handler with this function call is being
        // overridden here.
        // TODO: Fix this when we correct shadowbox_init.js to not insert
        // functions in the global namespace
        shadowbox_on_open();
    },

    process_credit: function() {
        // Format the title text for a better presentation atop the photo.
        // Intended to be called using the Shadowbox onFinish handler.

        var title_element = $('#sb-title-inner').first();
        var title_text = title_element.html();

        // Parse and mark up the title text.

        var parts = title_text.split(' ~ ');
        var image_title = parts[0];
        
        var copyright_holder = 'Copyrighted image.';
        if (parts[1]) {
            copyright_holder = parts[1];
        }
        
        var copyright = 'Copyright information coming soon.';
        if (parts[2] && $.trim(parts[2]).length > 0) {
            copyright = parts[2];
        }
        
        var source = '';
        if (parts[3]) {
            source = parts[3];
        }

        var title_parts = image_title.split(':');
        var image_type = title_parts[0];
        var title = image_type;
        var name = '';
        // Get the properly-italicized scientific name from the page heading,
        // if available, such as on the species page. Otherwise, just
        // italicize the entire plant name portion of the title for now. This
        // will generally be correct for the groups and subgroups pages'
        // galleries, which tend not to show varieties, subspecies, etc.
        var scientific_name = $('h2 .scientific');
        if (scientific_name.length > 0) {
            name = $.trim(scientific_name[0].innerHTML) + '.';
        }
        else if (title_parts[1] !== undefined) {
            name = '<i>' + $.trim(title_parts[1]) + '</i>';
        }
        if (name.length > 0) {
            title += ': ' + name;
        }

        var html = '<div><h6>' + title + '</h6><span>' + copyright_holder +
            ' ' + copyright + ' <a href="/terms-of-use/#ip" ' +
            'target="_blank">Terms of Use' + '</a></span>';
        if (source !== '') {
            html += '<br><span>' + parts[3] + '</span>';
        }
        html += '</div>';
        title_element.html(html);

        // Show the title element again.
        title_element.removeClass('hidden');
    }

};

// Create a small factory method to return, which will act
// as a little instance factory and constructor, so the user
// can do as follows:
// var obj = MyClassName(something, somethingelse);
function factory() {
    var instance = Object.create(PhotoHelper);
    instance.init();
    return instance;
}

return factory;

});
