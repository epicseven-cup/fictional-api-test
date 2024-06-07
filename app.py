import flask
app = flask('Hello')
@app.get('/users')
def respond_get_users():
	return 'Get Rounte /users was hit'