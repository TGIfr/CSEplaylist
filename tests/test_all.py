import unittest

import id3
import htmltags
import nesting
import xmlHelper


class TestMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    #id3
    def test_get_genre(self):
        self.assertTrue(id3.get_genre("http://ol7.mp3party.net/online/8500/8500219.mp3") == "Unknown")
        self.assertTrue(id3.get_genre("http://ol7.mp3party.net") == "Unknown")
        self.assertTrue(id3.get_genre("http://ol5.mp3party.net/online/7813/7813030.mp3") == ['Alternative'])

    #htmltags
    def test_hrefs(self):
        self.assertTrue(htmltags.hrefs("http://mp3party.net/music/8500219", nested=0) == set())
        set1 = {'https://litworld.herokuapp.com/contacts', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/search'}
        set2 = {'https://litworld.herokuapp.com/contacts', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/search', 'https://litworld.herokuapp.com/'}
        set3 = {'https://litworld.herokuapp.com/contacts'}
        self.assertTrue(sorted(htmltags.hrefs("https://litworld.herokuapp.com/", nested=1)) == sorted(set1))
        self.assertTrue(sorted(htmltags.hrefs("https://litworld.herokuapp.com/", nested=3)) == sorted(set2))
        self.assertFalse(htmltags.hrefs("http://mp3party.net/music/8500219", nested=0) == sorted(set3))

    def test_mp3refs(self):
        self.assertTrue(htmltags.mp3refs("http://mp3party.net/music/8500219") == ['http://ol7.mp3party.net/online/8500/8500219.mp3'])

    #nesting.py
    def test_get_nested_links(self):
        links1 = ['https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/search', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/contacts']
        links2 = ['https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/search', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/contacts', 'https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/register/signup', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/register/signup', 'https://litworld.herokuapp.com/search', 'https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/register/signup', 'https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/register/signup', 'https://litworld.herokuapp.com/contacts']
        self.assertTrue(nesting.get_nested_links("https://litworld.herokuapp.com/", 1) == links1)
        links3 = ['https://litworld.herokuapp.com/', 'https://litworld.herokuapp.com/world', 'https://litworld.herokuapp.com/search', 'https://litworld.herokuapp.com/register/login', 'https://litworld.herokuapp.com/contacts', 'https://litworld.herokuapp.com/register/signup', 'https://litworld.herokuapp.com/login']
        self.assertTrue(nesting.get_nested_links("https://litworld.herokuapp.com/", 3) == links3)
        self.assertTrue(nesting.get_nested_links("https://litworld.herokuapp.com/", 0) == [])
        self.assertTrue(nesting.get_nested_links_from_list(links1) == links2)

    #xmlHelper
    def test_parse(self):
        print(xmlHelper.save('tests/test1.xml', 's'))
        self.assertTrue(xmlHelper.parse('tests/test.xml') == [])
        test = '<songs><song>s</song></songs>'
        self.assertTrue(xmlHelper.save('tests/test1.xml', 's') == test)


if __name__ == '__main__':
    unittest.main()
