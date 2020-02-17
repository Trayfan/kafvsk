from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-827, REG-964 Е-Гарант полисы GetEgarantPolicy Проверить заполнение ответа при успешном запросе информации по договору, заключенному в Е-Гарант (Errors.Code=0)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\egarant\REG_827_REG_964\GetEgarantPolicy\Code_0"
        self.REQUEST_FILE = r"GetEgarantPolicyRequest.json"
        self.RESPONSE_FILE = r"GetEgarantPolicyResponse.json"
        self.request_topic = r"EgarantRequest"
        self.response_topic = r"EgarantResponse"
        MainTest.__init__(self)

