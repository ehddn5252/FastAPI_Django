import logging


class Logger:
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s::%(name)s::%(levelname)s - %(filename)s|%(lineno)d]  메세지[ %(message)s ]" , datefmt="%Y년%m월%d일 %H시:%M분:%S초")
    # formatter = logging.Formatter("[%(asctime)s::%(name)s::%(levelname)s - %(funcName)s|%(lineno)d]  메세지[ %(message)s ]" , datefmt="%Y-%m-%dT%H:%M:%S")
    ch.setFormatter(fmt=formatter)

    fh = logging.FileHandler(filename="DB.log" , mode="at" , encoding="utf-8")
    fh.setLevel(level=logging.ERROR)
    fh.setFormatter(fmt=formatter)

    logger = logging.Logger(name="로깅클래스" , level=logging.INFO)
    logger.setLevel(level=logging.INFO)
    logger.addHandler(hdlr=ch)
    logger.addHandler(hdlr=fh)
