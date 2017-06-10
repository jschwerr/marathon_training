$(document).ready(function() {
    /*when user selects a different runner
    only show data about that runner */
    $(".runner-select").change(function() {
        var selectVal = $(".runner-select").val();
        var selectDiv = "goal-";

        if (selectVal == "all") {
            $('.runner-goal').each(function() {
                $(this).removeClass("hide");
            });
        }
        else {
            selectDiv += selectVal.toString();
            $('.runner-goal').each(function() {
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