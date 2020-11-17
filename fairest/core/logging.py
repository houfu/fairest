import logging


def init_logger():
    logger = logging.getLogger('fairest')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


fairest_logger = logging.getLogger('fairest')
