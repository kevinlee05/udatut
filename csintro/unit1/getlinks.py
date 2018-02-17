# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/sample/">'''

page2 = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/sample2/">'''

def geturl(page):
    start_link = page.find('<a href=')
    start_quote = page.find('\"',start_link)
    start_url = start_quote+1
    end_quote = page.find('\"', start_quote+1)
    url = page[start_url:end_quote]
    return url

import unittest

class testgeturl(unittest.TestCase):
    def test(self):
        self.assertEqual(geturl(page), "/sample/")
        self.assertEqual(geturl(page2), "/sample2/")

if __name__ == "__main__":
    unittest.main()
