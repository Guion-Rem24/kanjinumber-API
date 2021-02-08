function visualize_kanji() {
    var kanji = document.getElementById("kanji").value
    console.log("get kanji:" + kanji)
    var api_url = "https://5nbkfno7nd.execute-api.ap-northeast-1.amazonaws.com/v1/kanji2number/"
    document.getElementById("result").innerHTML = kanji
}