import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    test the behaviour of News class
    '''
    def setUp(self):
        '''
        method to run before each class
        '''
        self.new_news = News(1234, 'Corona virus', 'flask is fucked up','moringa is also fucked fuckity up')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == "__main__":
    unittest.main()