import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FrontendTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_reply_drafting_interface(self):
        driver = self.driver
        driver.get("http://www.your-web-app-url.com")
        self.assertIn("Auto Email Reply Drafter", driver.title)
        elem = driver.find_element_by_id("replyDraftingInterface")
        self.assertIsNotNone(elem)

    def test_feedback_interface(self):
        driver = self.driver
        driver.get("http://www.your-web-app-url.com")
        elem = driver.find_element_by_id("feedbackInterface")
        self.assertIsNotNone(elem)

    def test_suggested_replies(self):
        driver = self.driver
        driver.get("http://www.your-web-app-url.com")
        elem = driver.find_element_by_id("suggestedReplies")
        self.assertIsNotNone(elem)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()