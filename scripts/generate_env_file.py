import os
from mpharma_challenge.settings.base import BASE_DIR

from scripts.util import logger

SECRET_KEY=os.environ.get('SECRET_KEY')

DATABASE_URL=os.environ.get('DATABASE_URL')

env_file = os.path.join(BASE_DIR, '.env')
try:
    with open(env_file, 'w') as file:
        file.write("SECRET_KEY={}".format(SECRET_KEY))
        file.write('\n')
        file.write("DATABASE_URL={}".format(DATABASE_URL))
    logger.info(".env file creation complete")
except Exception as e:
    logger.exception(e)
    logger.debug(".env file creation error")