$(document).ready(function() {

    function get_runner_data(runner_id) {
        url = '/training_tracker/ajax/edit_runner/' + runner_id;
        return $.get(url);
    };
//
//    var csrftoken = Cookies.get('csrftoken');
//
//    function csrfSafeMethod(method) {
//        // these HTTP methods do not require CSRF protection
//        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//    }
//
//    function edit_runner(runner_id) {
//        $.ajaxSetup({
//            beforeSend: function(xhr, settings) {
//                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
//                }
//            }
//        });
//        url = '/training_tracker/post_edit_runner/' + runner_id;
//        $.ajax({
//            url: url,
//            method: "POST",
//            contentType: "application/x-www-form-urlencoded"
//        });
//    }


    $('.runner-select').change(function() {
            if ($('.runner-select').val() != "all") {
                get_runner_data($('.runner-select').val()).done(function(data){
                    data = data[0]
                    $('#edit-runner-name').attr('value',data["name"]);
                    $('#edit-runner-age').attr('value',data["age"]);
                    $('#edit-runner-hours').attr('value',data["hours_goal"]);
                    $('#edit-runner-minutes').attr('value',data["minutes_goal"]);
                    $('#edit-runner-seconds').attr('value',data["seconds_goal"]);

                    var form_url = "/training_tracker/post_edit_runner/" + data["runner_id"]
                    $('#edit-runner-form').attr('action', form_url)
                });

            }
            else {
                $('#edit-runner-name').attr('value',"");
                $('#edit-runner-age').attr('value',"");
                $('#edit-runner-hours').attr('value',"");
                $('#edit-runner-minutes').attr('value',"");
                $('#edit-runner-seconds').attr('value',"");

                $('#edit-runner-form').attr('action','#');
            }
        }
    )

//    $('#edit-runner-form').on('submit', function(event) {
//        event.preventDefault();
//        edit_runner($('.runner-select').val());
//        return false;
//    });
});