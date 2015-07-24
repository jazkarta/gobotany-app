define([
    'bridge/jquery', 
    'bridge/jquery-ui', 
    'util/shadowbox_init',
    'util/formset',
    'util/suggester',
    'plantshare/checklist_form',
    'plantshare/upload_modal'
], function ($, jqueryUI, Shadowbox, formset, Suggester, ChecklistForm,
    upload_modal) {
    
    var UPLOAD_SPINNER = STATIC_URL + 'images/icons/preloaders-dot-net-lg.gif';

    var notes_modal = '' +
    '<div id="container" class="notes-modal">' +
		'<h1>Add Notes to Item</h1>' +
		'<section>' +
            '<textarea placeholder="Write your notes here"></textarea>' +
            '<div class="form-actions">' +
                '<a href="#" class="ps-button save orange-button caps">Save</a>' +
                '<a href="#" class="clear-btn">Clear</a>' +
            '</div><!-- /.form-actions -->' +
		'</section>' +
	'</div><!--!/#container -->';

    $(document).ready(function() {

        formset.init({
            'formSelector': '#formset tr',
            'formTemplateSelector': '#form-template tr',
            'addLinkSelector': '.add-new-row',
            'removeLinkSelector': '.close-btn.row-btn',
            'onAfterAddForm': ChecklistForm.set_tab_order
        });

        $('body').on('focus', 'input.date-input', function() {
            $(this).datepicker({dateFormat: 'mm/dd/yy'});
        });

        $('body').on('focus', 'input.suggest', function() {
            var suggester = new Suggester(this);
            suggester.setup();
        });

        // Shadowbox setup for Notes modal popups
        $(document).on('click', 'a.note-link', function(e) {
            e.preventDefault();
            var $this = $(this);
            Shadowbox.open({
                content:  notes_modal,
                player: 'html',
                title: 'Checklist Notes',
                width: 550,
                height: 240,
                options: {
                    enableKeys: false,
                    onFinish: function(item) {
                        var $textarea = $('#container').find('textarea');
                        var $field = $this.parents('td.note').find('textarea');
                        $textarea.val($field.val());
                        $textarea.attr('rel', $field.attr('id'));
                    }
                }
            });
        });
        $(document).on('click', '.notes-modal a.save', function(e) {
            e.preventDefault();
            var $textarea = $(this).parents('section').find('textarea');
            var $field = $('#' + $textarea.attr('rel'));
            $field.val($textarea.val());
            Shadowbox.close();
        });
        $(document).on('click', '.notes-modal a.clear-btn', function(e) {
            e.preventDefault();
            $(this).parents('section').find('textarea').val('');
        });

        function startUpload($trigger) {
            console.log('Beginning upload...');
            $trigger.html('<img src="' + UPLOAD_SPINNER + '" class="checklist-thumb">');
        }

        function imageUploaded(imageInfo, $trigger) {
            console.log('Successfully uploaded checklist image');
            $trigger.html('<img src="' + imageInfo.thumb + '" class="checklist-thumb">');
            $trigger.parent().find('input[type="hidden"]').val(imageInfo.id);
        }

        function uploadError(errorInfo, $trigger) {
            console.log('Checklist image upload error: ' + errorInfo);
        }

        upload_modal.setup('.image-modal', '.upload-image-thumb', {
            onUploadComplete: imageUploaded,
            onError: uploadError,
            onStartUpload: startUpload,
        });

        // Start at the first field to fill out: the checklist title.
        $('#id_name').focus();

        // Set the tab order on the initial checklist entry row.
        ChecklistForm.set_tab_order();
    });
});
