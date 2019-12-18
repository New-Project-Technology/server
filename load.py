# class Flask
from flask import Flask, jsonify, request
app = Flask (__name__)

app.users = {}
app.id_count = 1

@app.route("/", methods=['GET','POST'])
def postdata():
    jsonDdata = request.get_json()
    print jsonData['id']
    print jsonData['Name']
    return response

#package.json 전체 내려받기
@app.route('/package.json')
def package():
    response = make_response(render_template('package.json'))
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response

def sign_in():
    if request.method == 'GET':
        return ren

def sign_in():
    new_user = request.json
    new_user["userId"] = app.id_count
    app.users[app.id_count] = new_user
    
#실행함수 run
if __name__ == '__main__':
    app.run()
