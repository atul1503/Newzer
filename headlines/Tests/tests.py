from django.test import TestCase

# Create your tests here.
class headliner(TestCase):
    def test(self):
        response=self.client.get('/top_headlines')
        self.assertEqual(response.status_code,200)
        prev_categ=self.client.session['pref']['categ']
        self.client.get('/top_headlines',{'categ':'health'})
        self.assertNotEqual(self.client.session['pref']['categ'],prev_categ)
    
    def test1(self):
        response=self.client.get('/top_headlines')
        self.assertEqual(response.status_code,200)
        prev_categ=self.client.session['pref']['categ']
        self.client.get('/top_headlines',{'next':''})
        self.assertEqual(self.client.session['pref']['categ'],prev_categ)
        
    def test2(self):
        response=self.client.get('/top_headlines',{'categ':'health'})
        self.client.get('/top_headlines',{'next':''})
        self.client.get('/top_headlines',{'next':''})
        self.client.get('/top_headlines',{'next':''})
        self.assertEqual(self.client.session['pref']['categ'],'health')
        
