API_ENDPOINT = "127.0.0.1:5001"

function run() {
    $.get(API_ENDPOINT + "/hosts", function (data) {
        for(var i = 0; i < data.length; i++){
            console.log(data[i])
        }
    });
}