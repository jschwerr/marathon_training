
$(document).ready(function() {

    $('.accordion .accordion-section-content').hide();

    function close_accordion_section() {
        $('.accordion .accordion-section-title').removeClass('active');
        $('.accordion .accordion-section-content').slideUp(300).removeClass('open');
        $('.accordion .accordion-section-title').addClass('collapsed')
    }
    $('.accordion-section-title').click(function(e) {
        // Grab current anchor value
        var currentAttrValue = $(this).attr('id');

        if($(e.target).is('.active')) {
            close_accordion_section();
        }else {
            close_accordion_section();

            // Add active class to section title
            $(this).addClass('active');
            // Open up the hidden content panel
            $('.accordion ' + currentAttrValue).slideDown(300).addClass('open');
            $(this).removeClass('collapsed');
        }

        e.preventDefault();
    });

    /* view-runs.html when user selects a different runner
       only show data about that runner */
    $(".runner-select").change(function() {
        var selectVal = $(".runner-select").val();
        var selectDiv = "run-history-info-";

        if (selectVal == "all") {
            $('.run-history-info').each(function() {
                $(this).removeClass("hide");
            });
        }
        else {
            selectDiv += selectVal.toString();
            $('.run-history-info').each(function() {
                if ($(this).attr('id') != selectDiv) {
                    $(this).addClass("hide");
                }
                else {
                    $(this).removeClass("hide");
                }
            });
        }
    });

})