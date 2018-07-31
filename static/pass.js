function CheckPass(input){
    var pass    = document.getElementById ( 'pass'    ); //パスフォームの値を取得
    var passCon = document.getElementById ( 'passCon' ); //パス確認用フォームの値を取得
/*
    var pass        = pass.value; //パスフォームの値を取得
    var passConfirm = input.value; //パス確認用フォームの値を取得(引数input)
*/
    // パスワードの一致確認
    if ( pass != passCon ){
        input.setCustomValidity ( 'パスワードが一致しません' ); // エラーメッセージのセット
    } else {
        input.setCustomValidity ( '' ); // エラーメッセージのクリア
    }
}


function CheckPassword(confirm){
    // 入力値取得
    var input1 = password.value;
    var input2 = confirm.value;
    // パスワード比較
    if(input1 != input2){
        confirm.setCustomValidity("入力値が一致しません。");
    }else{
        confirm.setCustomValidity('');
    }
}


