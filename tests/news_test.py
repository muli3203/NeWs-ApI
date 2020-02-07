import unittest
from app.models import News, Articles

#since i've imported the class names from models, the line below is not required.
# News = news.News

class NewsTest(unittest.TestCase):
    '''
    test the behaviour of News class
    '''
    def setUp(self):
        '''
        method to run before each class
        '''
        self.new_news = News(id,name,description,url,category,language,country)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

#the run command below has been commented out because the unittests will be run from manage.py
#if __name__ == "__main__":
 #   unittest.main()