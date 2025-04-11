from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xf7`\xcf\xe1wS\x18\xaa\x1f\xd0\xed\x93Y+\x9f\xb3'