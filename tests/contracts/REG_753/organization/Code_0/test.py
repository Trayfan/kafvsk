from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self):
        self.PATH = r".\tests\contracts\REG_753\organization\Code_0"
        self.REQUEST_FILE = r"CheckSubjectObjectOrganizationRequest.json"
        self.RESPONSE_FILE = r"CheckSubjectObjectOrganizationResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
