
from flaskblog.secrets import Secrets

class Config:
	secretsObj=Secrets()
	SECRET_KEY=secretsObj.SECRET_KEY
	SQLALCHEMY_DATABASE_URI=secretsObj.DATABASE_URI
	MAIL_SERVER='smtp.googlemail.com'
	MAIL_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=secretsObj.EMAIL_ADDRESS
	MAIL_PASSWORD=secretsObj.PASSWORD
