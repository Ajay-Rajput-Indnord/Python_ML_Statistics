import logging
logger=logging.getLogger(__name__)

logger.setLevel(logging.INFO)

consolhandler=logging.StreamHandler()
filehandler=logging.FileHandler('app.log')

# logger.addHandler(consolhandler)
# logger.addHandler(filehandler)

#logger.info('this is out put')

consolhandler.setLevel(logging.WARNING)
filehandler.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s | %(name)s | %(namelevel)s | %(message)s')
consolhandler.setFormatter(formatter)
logger.addHandler(consolhandler)
logger.warning('done done')