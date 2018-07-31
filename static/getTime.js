function set2fig    ( num ) {
// 桁数が1桁だったら先頭に0を加えて2桁に調整する
    var ret;
    if( num < 10 ) { ret = "0" + num; }
    else           { ret =       num; }
    return ret;
}
function showClock2 (     ) {
    var nowTime = new Date ( );

    var Month   = set2fig ( nowTime.getMonth   ( ) );
    var Day     = set2fig ( nowTime.getdate    ( ) );
    var Hour    = set2fig ( nowTime.getHours   ( ) );
    var Min     = set2fig ( nowTime.getMinutes ( ) );
    var Sec     = set2fig ( nowTime.getSeconds ( ) );

    var msg     = "Final login : " +Month + "月" + Day + "日 " + nowHour + ":" + nowMin;

    document.getElementById ( "RealtimeClockArea2" ).innerHTML = msg;
}
setInterval ( 'showClock2 ( )', 1000 );
