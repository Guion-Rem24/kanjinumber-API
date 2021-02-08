function visualize_number() {
    var num = document.getElementById("number").value
    console.log("get number:" + num)
    var api_url = "https://5nbkfno7nd.execute-api.ap-northeast-1.amazonaws.com/v1/number2kanji/" + num;
    var request = new XMLHttpRequest();
    request.open('GET', api_url);
    request.setRequestHeader('Access-Control-Allow-Origin','*');
    request.setRequestHeader('Content-Type', 'application/json');
    request.setRequestHeader('Access-Control-Arrow-Headers','Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token');
    // request.setRequestHeader('')
    // request.responseType = 'json';

    request.onload = function () {
        document.getElementById("result_json").innerHTML = this.responce;
    }
    request.send();
    document.getElementById("result").innerHTML = num;
}