import logging
import inspect

def custom_logger(logLevel=logging.DEBUG):
    """Функция инициализации логгера
    
    Keyword Arguments:
        logLevel {} --  (default: {logging.DEBUG})
    
    Returns:
        [type] -- экземпляр логгера
    """
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('TestLog.log', mode='w', encoding='utf-8')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger