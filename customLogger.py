import logging
import inspect
from shutil import copyfile


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
    
    file_handler = logging.FileHandler('test_log.log', mode='w', encoding='utf-8')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter(u'%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def generate_test_report(logger):
    try:
        with open('test_report.csv', 'w', encoding='utf-8') as test_report:
            with open('test_log.log', 'r', encoding='utf-8') as test_log:
                test_report_body = "Название теста,Результат теста\n"
                new_line = ""
                is_start = 1
                is_end = 0
                for string in test_log.readlines():
                    if " # " in string:
                        if is_start:
                            new_line += string.split("Start test ")[1][:-1] + ","
                            is_start = 0
                            is_end = 1
                            continue
                        if is_end:
                            new_line += string.split(" # ")[1]
                            test_report_body += new_line
                            new_line = ""
                            is_end = 0
                            is_start = 1
                            continue
                test_report.write(test_report_body)
    except Exception as err:
        logger.error(f"ERROR generate_test_report: {err}")