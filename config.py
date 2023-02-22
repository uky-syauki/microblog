import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(os.environ.get('MAIL_USERNAME'))
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	MAIL_SERVER = 'smtp.gmail.com'  #os.environ.get('MAIL_SERVER')
	MAIL_PORT = 587  #int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = 1  #os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = "info.blog.uki@gmail.com"  #os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = "nhfeeiuutruywcrz"  #os.environ.get('MAIL_PASSWORD')
	ADMINS = ['info.blog.uki@gmail.com']
	POSTS_PER_PAGE = 25
	LANGUAGES = ['en', 'ind']
