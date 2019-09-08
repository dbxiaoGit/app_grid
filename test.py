import logging

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler1 = logging.FileHandler('test.log', 'w', 'utf-8')
    handler1.setFormatter(logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s' ))
    handler2 = logging.StreamHandler()
    handler2.setFormatter(logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s' ))
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.info('info')
    logger.debug('debug')
    logger.error('error')
