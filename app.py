from flask import Flask, jsonify, render_template
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def assignment12_home():
    return render_template('Assignment12.html')

@app.route('/assignment12/restapi_users/', defaults={'user_id': 1})  # default - dictionary of variables
@app.route('/assignment12/restapi_users/<int:user_id>')
def assignment12_func(user_id):
    query = 'select * from users where id = %s;' % user_id
    users = interact_db(query, 'fetch')
    return_dict = {}
    if len(users) == 0:  # didnt get a user from the db
        return_dict = {
            'Result': 'Failure',
            'Message': 'There is no user with this id, try again'
        }
    else:
        return_dict[f'User_{user_id}'] = {
            'Result': 'Success',
            'ID': users[0].id,
            'Name': users[0].name,
            'Email': users[0].email
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)
