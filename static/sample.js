var form = document.forms[0];
form.onsubmit = function() {
    // エラーメッセージをクリアする
    form.password.setCustomValidity("");
    // パスワードの一致確認
    if (form.password.value != form.passwordConfirm.value) {
        // 一致していなかったら、エラーメッセージを表示する
        form.password.setCustomValidity("パスワードと確認用パスワードが一致しません");
    }
};
// 入力値チェックエラーが発生したときの処理
form.addEventListener("invalid", function() {
    document.getElementById("errorMessage").innerHTML = "入力値にエラーがあります";
}, false);

