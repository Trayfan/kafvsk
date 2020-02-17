from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-583, REG-820 КБМ Проверить заполнение ответа при указании невалидного значения атрибута Type (Errors.Code=1)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\kbm\REG_583_REG_820\get_kbm\Type"
        self.REQUEST_FILE = r"GetKbmRequest.json"
        self.RESPONSE_FILE = r"GetKbmResponse.json"
        self.request_topic = r"KbmRequest"
        self.response_topic = r"KbmResponse"
        MainTest.__init__(self)

