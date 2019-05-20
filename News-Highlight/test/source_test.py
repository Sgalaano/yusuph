import unittest
from app.models import Source,news

class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source Class
    """
    def setup(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source("bloomberg","Galaano suleiman","Test to see if Source is retrieved","TestUrl","The article itself")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_source.id,"bloomberg")
        self.assertEqual(self.new_source.name,"Galaano suleiman")
        self.assertEqual(self.new_source.description,"Test to see if Source is retrieved")
        self.assertEqual(self.new_source.url,"TestUrl")
        self.assertEqual(self.new_source.category,"The article itself")

class ArticleTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """
    def setup(self):
        """
        Set up method that will run before every Test
        """
        self.new_article = Article("bloomberg","TestTitle","TestDescription","TestUrl","TestUrlToImage","TestPublishedAt","TestContent")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_article.id,"bloomberg")
        self.assertEqual(self.new_article.title,"TestTitle")
        self.assertEqual(self.new_article.description,"TestDescription")
        self.assertEqual(self.new_article.url,"TestUrl")
        self.assertEqual(self.new_article.urlToImage,"TestUrlToImage")
        self.assertEqual(self.new_article.publishedAt,"TestPublishedAt")
        self.assertEqual(self.new_article.content,"TestContent")
