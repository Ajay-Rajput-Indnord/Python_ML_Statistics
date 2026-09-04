import logging
import time

logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s' )
######basic####
# s=time.time()
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# e=time.time()
# #print(s-e)

### variable ###
# x=2
# logging.info(f'the value is {x}')

### try and except
# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error('ZeroDivisionError',exc_info=True)

###custom logger
logger=logging.getLogger(__name__)
#adding handler
handler=logging.FileHandler('text.log')
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('testing the logger')