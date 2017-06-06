$(document).ready(function() {

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