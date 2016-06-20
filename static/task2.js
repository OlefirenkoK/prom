var base_message = 'Рад тебя видеть снова,',
    epithets = null,
    EPITHETS = null;

function getCookie(name){
    var re = new RegExp(name + '=([^;]+)'),
        value = re.exec(document.cookie);
    return (value != null) ? unescape(value[1]) : null;
}


function getCookieValues(){
    var re = new RegExp('[^;\s]+=([^;]+)', 'g'),
        cookieValues = [],
        match;
    while ( ( match = re.exec(document.cookie) ) != null ) {
        cookieValues.push(match[1]);
    }
    return cookieValues;
}


function getEpithet(name){
    var names_epithet = getCookie(name);
    if (!names_epithet) {
        var ep = epithets[Math.floor(Math.random() * epithets.length)];
        epithets.pop(ep);
        if (epithets.length === 0){
            epithets = EPITHETS.slice();
        }
        document.cookie = name + '=' + ep;
        return ep;
    } else {
        return names_epithet;
    }
}


function newName() {
    var obj = document.getElementById('name'),
        message = document.getElementById('message');
    if (obj.value) {
        var epitet = getEpithet(obj.value);
        document.cookie = obj.value + '=' + epitet;
        message.textContent = base_message + ' ' + obj.value + ' ' + epitet
        obj.value = '';
    }
}

function getEpithets(){
    $.get(
        '/epithets/',
        function(data){
            if (!epithets){
                EPITHETS = JSON.parse(data);
                epithets = DiffArrays(EPITHETS, getCookieValues());
            }
        }
    )
}

function DiffArrays(A,B){
    var M = A.length, N = B.length, c = 0, C = [];
    for (var i = 0; i < M; i++) {
        var j = 0,
            k = 0;
        while (B[j] !== A[ i ] && j < N) j++;
        while (C[k] !== A[ i ] && k < c) k++;
        if (j == N && k == c) C[c++] = A[ i ];
    }
    return C;
}

$(document).ready(function(){
    getEpithets();
});
