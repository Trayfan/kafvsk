from MainTest import MainTest


class Test_sub(MainTest):
    def __init__(self, cl):
        self.logger = cl
        self.test_name = r"REG-772 AccrualDate Загрузка даты начисления/возврата страховой премии (договора)"
        self.logger.info(f"# Start test {self.test_name}")

        self.PATH = r".\tests\contracts\REG_772\contract\Code_0"
        self.REQUEST_FILE = r"ChangeContractPremiumDateRequest.json"
        self.RESPONSE_FILE = r"ChangeContractPremiumDateResponse.json"
        self.request_topic = r"ContractsRequest"
        self.response_topic = r"ContractsResponse"
        MainTest.__init__(self)
