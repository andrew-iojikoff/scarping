"""
@package base

GUIBaseTestCase class implementation

This class consists of all the initialization, setup and teardown functionality

This class is inherited by all the test classes
It should not be used by creating an object instance

@author Anil Tomar <anil.tomar@nimblestorage.com>
@version 1.0
@copyright Nimble Storage, Inc

Example:
    class ChapAccountsTest(GUIBaseTestCase)
"""
from base.webdriverfactory import WebDriverFactory
from nimble.log.logger import *
from nimble.test.nimblebasetestcase import NimbleBaseTestCase
from pages.home.login_page import LoginPage
from pages.home.navigation import Navigation
from utilities.be_connection import BEConnection
from utilities.checkpoint import CheckPoint
from utilities.util import Util
import time


#from nimble.test.tcspec import TestCaseSpec


class BaseTestCase():

    def __init__(self):
        pass

    def setUp(self):
        # In the setup() or __init__(), config file should be parsed
        self.login.login("admin", "admin")

    def tearDown(self):
        self.log.info("Driver quit, session closed")
