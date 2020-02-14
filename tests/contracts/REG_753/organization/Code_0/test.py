from MainTest import MainTest
import customLogger as cl



class Test_sub(MainTest):
    def __init__(self):
        self.logger = cl.custom_logger()
        self.test_name = r"qwe"
        self.logger.info(f"# Start test {self.test_name}")
        self.PATH = r".\tests\contracts\REG_753\organization\Code_0"
        self.REQUEST_FILE = r"CheckSubjectObjectOrganizationRequest.json"
        self.RESPONSE_FILE = r"CheckSubjectObjectOrganizationResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsRequest"
        MainTest.__init__(self)
