import logging

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('myapp.log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

logger.error('ERROR occured')
logger.info("HERE WE ARE")
