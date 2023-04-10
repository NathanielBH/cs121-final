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

homeButton.click(function(){
    window.location.href = "/home_page.html";
})