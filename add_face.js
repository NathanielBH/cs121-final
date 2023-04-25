$(document).ready(function() {
    var button = $("#add_button");
    var message = $("#message");
    var homeButton = $("#home");

    button.click(function() {
        console.log(button.text());
        if (button.text() === "Add Face") {
            $.ajax({
                url: "/add_face",
                type: "post",
                success: function(response) {
                    console.log(response);
                    button.text("Scanning");
                    message.text("Scanning in progress...");
                }
            });
        } else if (button.text() === "Scanning") {
            message.text("Face Scan Successful");
            button.text("Add Face");
        } else {
        $.ajax({
            url: "/stop_add",
            type: "post",
            success: function() {
                button.text("Add Face");
                message.text("Scan successful!");
                message.fadeOut(3000); // optional: hide message after 3 seconds
            }
        })
    }
});

    $('#add_form2').submit(function(event) {
        event.preventDefault();
        var name = $('#fname').val();
        $.ajax({
            type: 'POST',
            url: '/add_face',
            data: JSON.stringify({'name': name}),
            contentType: 'application/json',
            success: function(response) {
                $('#message').text(response.message);
            }
        });
    });

    homeButton.click(function(){
        console.log(homeButton.text())
        if (homeButton.text() === "Home") {
            $.ajax({
                url: "/",
                type: "post",
                success: function(response) {
                    console.log(response);
                }
            });
        }
    });
});


