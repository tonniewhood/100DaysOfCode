
var redirect_url = "http://127.0.0.1:5500/index.html";

var client_id = "c2b3b3c0-7b1a-4b7e-8b1a-5b9b7b1a4b7e";
var secret_id = "c2b3b3c0-7b1a-4b7e-8b1a-5b9b7b1a4b7e";

const AUTHORIZE_ENDPOINT = "https://accounts.spotify.com/authorize";

function requestAuth(){
    
    let url = AUTHORIZE_ENDPOINT;
    url += "?client_id=" + client_id;
    url += "&response_type=code";
    url += "&redirect_uri=" + encodeURI(redirect_url);
    url += "&show_dialog=true";
    url += "&scope=user-read-private%20user-read-email%20user-modify-private";
    window.location.href = url;
}