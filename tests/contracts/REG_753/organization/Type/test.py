from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-753 CheckSubjectObject (Моки) Запрос на вызов проверки субъекта/объекта ЮЛ (Type = «Organization2») (Errors. Code=1) (Невалидный Type)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\contracts\REG_753\organization\Type"
        self.REQUEST_FILE = r"CheckSubjectObjectOrganizationRequest-invalidType.json"
        self.RESPONSE_FILE = r"CheckSubjectObjectOrganizationResponse-invalidType.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
