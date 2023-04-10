var button = $("#scan_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "Scan Face") {
        $.ajax({
            url: "/start_scan",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("Scanning");
            }
        });
    } else {
        $.ajax({
            url: "/stop_scan",
            type: "post",
            success: function() {
                button.text("Scan Face");
            }
        })
    }
});
