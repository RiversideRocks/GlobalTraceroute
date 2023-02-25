API_ENDPOINT = "http://192.168.0.8:5000"

function run() {
    $.get(API_ENDPOINT + "/hosts", function (data) {
        for(var i = 0; i < data.length; i++){
            console.log(data[i])
        }
    });
}