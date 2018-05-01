import os
import shutil

from boa_test.tests.boa_test import BoaFixtureTest
from boa.compiler import Compiler
from neo.Prompt.Commands.BuildNRun import TestBuild
from neo.Settings import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings.USE_DEBUG_STORAGE = False


class TestBookmarkContract(BoaFixtureTest):
    dispatched_events = []
    dispatched_logs = []

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_is_invalid_operation(self):
        output = Compiler.instance().load('%s/nos_bookmark.py' % BASE_DIR)
        out = output.write()

        tx, results, total_ops, engine = TestBuild(out, ['into_the_void', '[]'], self.GetWallet1(), '0705', '05')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].GetBoolean(), False)
