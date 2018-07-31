from flask import Flask, render_template, request

app = Flask ( __name__ )

@app.route ( '/' )
def index ( ) -> str :
    return render_template ( 'index.html' )

@app.route ( '/index', methods = [ 'GET', 'POST' ] )
def getpost ( ) -> str :
    if   request.method == 'GET'  :
        return render_template ( 'mypage.html' )
    elif request.method == 'POST' :
        res = request.form     [ 'post_value' ]
    return res

@app.route  ( '/query' )
def QueryHome   ( ) -> str :
    return render_template ( 'query.html' )

@app.route  ( '/login' )
def LoginMenu   ( ) -> str :
    return render_template ( 'login.html' )

@app.route  ( '/login/mypage', methods = [ 'GET', 'POST' ] )
def MyPage  ( ) -> str :
    if   request.method == 'GET'  :
        res = render_template ( 'mypage.html' )
    elif request.method == 'POST' :
        res = render_template ( 'login.html' )
    return res

@app.route  ( '/login/newAcc', methods = [ 'GET', 'POST' ] )
def newAccount  ( ) -> str :
    if   request.method == 'GET'  :
        return render_template ( 'createAccount.html' )
    elif request.method == 'POST' :
        res = request.form     [ 'post_value' ]
    return res


if __name__ == "__main__" :
    print ( "test" )
    app.debug = True
    app.run ( host = '127.0.0.1', port = 8888 )

