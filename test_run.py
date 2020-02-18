import customLogger as cl
logger = cl.custom_logger()


import tests.contracts.REG_753.organization.Code_0.test
import tests.contracts.REG_753.organization.Method.test
import tests.contracts.REG_753.organization.Type.test
import tests.contracts.REG_753.person.Code_0.test
import tests.contracts.REG_753.vehicle.Code_0.test
tests.contracts.REG_753.organization.Code_0.test.Test_sub(logger).test()
tests.contracts.REG_753.organization.Method.test.Test_sub(logger).test()
tests.contracts.REG_753.organization.Type.test.Test_sub(logger).test()
tests.contracts.REG_753.person.Code_0.test.Test_sub(logger).test()
tests.contracts.REG_753.vehicle.Code_0.test.Test_sub(logger).test()


# import tests.contracts.REG_578.BSO.Code_0.test
# import tests.contracts.REG_578.DraftContractForClosing.Code_0.test
# import tests.contracts.REG_578.BSOAddendum.Code_0.test
# import tests.contracts.REG_578.DraftAddendum.Code_0.test
# import tests.contracts.REG_578.DraftContractForClosing.Method.test
# import tests.contracts.REG_578.DraftContractForClosing.Type.test
# tests.contracts.REG_578.DraftContractForClosing.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftContractForClosing.Method.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftContractForClosing.Type.test.Test_sub(logger).test()
# tests.contracts.REG_578.BSO.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.BSOAddendum.Code_0.test.Test_sub(logger).test()
# tests.contracts.REG_578.DraftAddendum.Code_0.test.Test_sub(logger).test()


# import tests.kbm.REG_583_REG_820.get_kbm.person_1.test
# import tests.kbm.REG_583_REG_820.get_kbm.person_2.test
# import tests.kbm.REG_583_REG_820.get_kbm.organization_1.test
# import tests.kbm.REG_583_REG_820.get_kbm.Method.test
# import tests.kbm.REG_583_REG_820.get_kbm.Type.test
# tests.kbm.REG_583_REG_820.get_kbm.person_1.test.Test_sub(logger).test()
# tests.kbm.REG_583_REG_820.get_kbm.person_2.test.Test_sub(logger).test()
# tests.kbm.REG_583_REG_820.get_kbm.organization_1.test.Test_sub(logger).test()
# tests.kbm.REG_583_REG_820.get_kbm.Method.test.Test_sub(logger).test()
# tests.kbm.REG_583_REG_820.get_kbm.Type.test.Test_sub(logger).test()


# import tests.egarant.REG_827_REG_964.GetEgarantPoliciesId.Code_0.test
# import tests.egarant.REG_827_REG_964.GetEgarantPoliciesId.Method.test
# import tests.egarant.REG_827_REG_964.GetEgarantPolicy.Code_0.test
# import tests.egarant.REG_827_REG_964.GetEgarantPolicy.Method.test
# tests.egarant.REG_827_REG_964.GetEgarantPoliciesId.Code_0.test.Test_sub(logger).test()
# tests.egarant.REG_827_REG_964.GetEgarantPoliciesId.Method.test.Test_sub(logger).test()
# tests.egarant.REG_827_REG_964.GetEgarantPolicy.Code_0.test.Test_sub(logger).test()
# tests.egarant.REG_827_REG_964.GetEgarantPolicy.Method.test.Test_sub(logger).test()


cl.generate_test_report(logger)