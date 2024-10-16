from unittest import TestSuite, TestLoader, TextTestRunner

import tests_12_3

abc = TestSuite()
abc.addTest(TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
abc.addTest(TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = TextTestRunner(verbosity=2)
runner.run(abc)
