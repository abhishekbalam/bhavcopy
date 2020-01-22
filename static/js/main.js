$( document ).ready(function() {

    $(document).keypress(function (e) {
        var key = e.which;
        if(key == 13)
        {
        $("#submit").click();
        return false; 
        }
    });   

    $("#submit").click(function(){
        query = $("#search").val().trim();
        console.log(query);
        if(query !== ""){
            $.get( "/search", { name: $("#search").val().toUpperCase().trim() },
                function(data){
                    if(data.status){
                        $("#myTable").show();
                        $("#tableHeader").text("Search Results For: \""+query+"\"");
                        $("#myTable tbody tr").remove();
                        console.log(data.code)
                        rowdata = "<tr>" +
                                  "<td>" + data.code + "</td>" + 
                                  "<td>" + data.name + "</td>" +
                                  "<td>" + data.open + "</td>" +
                                  "<td>" + data.high + "</td>" +
                                  "<td>" + data.low + "</td>" +
                                  "<td>" + data.close + "</td>" +
                                  "</tr>"
                        console.log(rowdata);
                        $('#myTable > tbody:last-child').append(rowdata);
                    }
                    else{
                        $("#tableHeader").text("No stock found with name: \""+query+"\"");
                        $("#myTable").hide();
                    }
                })
                .fail(
                function(){
                    alert('Error: Server down, please try later.')
                });
        }
        else{
            location.reload();  
        }
    });
});
