from MainTest import MainTest
import customLogger as cl



class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-753 CheckSubjectObject (Моки) Запрос на вызов проверки субъекта/объекта ЮЛ (Type = «Organization») (Errors. Code=0)."
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\contracts\REG_753\organization\Code_0"
        self.REQUEST_FILE = r"CheckSubjectObjectOrganizationRequest.json"
        self.RESPONSE_FILE = r"CheckSubjectObjectOrganizationResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
