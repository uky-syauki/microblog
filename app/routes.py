from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'usename':'Ahmad Syauki'}
	return '''
	<html>
		<head><title>Hlaman Beranda</title></head>
		<body>
			<h1>Hello, ''' + user['username'] + '''!</h1>
		</body>
	</html>
	'''
