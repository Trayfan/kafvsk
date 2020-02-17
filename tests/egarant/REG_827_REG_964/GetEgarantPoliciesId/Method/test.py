from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-827, REG-964 GetEgarantPolicies Е-Гарант полисы Проверить заполнение ответа при указании невалидного значения атрибута Method (Errors.Code=1)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\egarant\REG_827_REG_964\GetEgarantPoliciesId\Method"
        self.REQUEST_FILE = r"GetEgarantPoliciesIdRequest.json"
        self.RESPONSE_FILE = r"GetEgarantPoliciesIdResponse.json"
        self.request_topic = r"EgarantRequest"
        self.response_topic = r"EgarantResponse"
        MainTest.__init__(self)

