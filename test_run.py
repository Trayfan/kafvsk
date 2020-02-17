import customLogger as cl
import tests.contracts.REG_753.organization.Code_0.test
import tests.contracts.REG_753.organization.Method.test
import tests.contracts.REG_753.organization.Type.test
import tests.contracts.REG_753.person.Code_0.test
import tests.contracts.REG_753.vehicle.Code_0.test
import tests.contracts.REG_578.BSO.Code_0.test
import tests.contracts.REG_578.DraftContractForClosing.Code_0.test
import tests.contracts.REG_578.BSOAddendum.Code_0.test
import tests.contracts.REG_578.DraftAddendum.Code_0.test
import tests.contracts.REG_578.DraftContractForClosing.Method.test
import tests.contracts.REG_578.DraftContractForClosing.Type.test
# import tests.kbm.REG_583_REG_820.get_kbm.person_1.test
# import tests.kbm.REG_583_REG_820.get_kbm.person_2.test
# import tests.kbm.REG_583_REG_820.get_kbm.organization_1.test

# import tests.contracts.REG_578.BSO.Code_0.test
# import tests.contracts.REG_578.BSO.Method.test


logger = cl.custom_logger()

tests.contracts.REG_753.organization.Code_0.test.Test_sub(logger).test()
tests.contracts.REG_753.organization.Method.test.Test_sub(logger).test()
tests.contracts.REG_753.organization.Type.test.Test_sub(logger).test()
tests.contracts.REG_753.person.Code_0.test.Test_sub(logger).test()
tests.contracts.REG_753.vehicle.Code_0.test.Test_sub(logger).test()

# tests.contracts.REG_578.DraftContractForClosing.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftContractForClosing.Method.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftContractForClosing.Type.test.Test_sub(logger).test()

# tests.contracts.REG_578.BSO.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.BSOAddendum.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftAddendum.Code_0.test.Test_sub(logger).test()
