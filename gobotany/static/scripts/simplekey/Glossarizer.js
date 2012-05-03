define([
    'ember',
    'jquery',
    'lib/tooltipsy'
], function() {return Ember.Object.extend({

    /* The glossarizer takes the glossary blob delivered by the API,
       parses and prepares a regular expression, and then can mark up
       glossary terms inside of text so that they turn into tooltipped
       terms. */

    _escape: function(str) {
        // http://stackoverflow.com/questions/3446170/
        return str.replace(/[-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, '\\$&');
    },

    init: function() {
        // this.glossaryblob must be provided in create()
        this.n = 0;
        var terms = [];
        var defs = this.glossaryblob.definitions;
        for (term in defs)
            if (_.has(defs, term))
                terms.push(this._escape(term));

        /* For incredible speed, we pre-build a regular expression of
           all glossary terms.  This has the advantage of always selecting
           the longest possible glossary term if several words together
           could be a glossary term! */
        var re = '\\b(' + terms.join('|') + ')\\b';
        this.regexp = new RegExp(re, 'gi');
    },

    /* Call "markup" on a node - hopefully one with no elements
       beneath it, but just text - to have its innerHTML scanned for
       glossary terms.  Any terms found are replaced with a <span>
       to which a Dijit tooltip is then attached. */

    markup: function(node) {
        node.innerHTML = node.innerHTML.replace(
            this.regexp, '<span class="gloss">$1</span>'
        );
        var self = this;
        var defs = this.glossaryblob.definitions;
        var images = this.glossaryblob.images;
        $('.gloss', node).each(function(i, node2) {
            self.n++;
            var gloss_id = 'gloss' + self.n;
            var term = node2.innerHTML.toLowerCase();
            var imgsrc = images[term];
            node2.id = gloss_id;
            $('#' + gloss_id).tooltipsy({
                content: '<p class="glosstip">' +
                    (imgsrc ? '<img src="' + imgsrc + '">' : '') +
                    defs[term] + '</p>',
                show: function(event, $tooltip) {
                    if (parseFloat($tooltip.css('left')) < 0)
                        $tooltip.css('left', '0px');
                    $tooltip.show();
                }
            });
        });
    }
})});