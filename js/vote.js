var votes = parseInt(document.getElementById("votenum").innerHTML);

function getVote (value) {
    votes++;
    $('#votenum').html(""+votes);
    confirm("ok");

    var i = 0;
    var vv = [0, 0, 0, 0]

    $('.vote').each(function() {
        vv[i] = parseInt($(this).attr('id'));
        i++;
    });

    vv[value]++;
    i = 0;

    $('.leg').each(function() {
        opt = parseInt($(this).attr('id'));
        $(this).html(""+(vv[opt]/votes)*100);
    });
}
