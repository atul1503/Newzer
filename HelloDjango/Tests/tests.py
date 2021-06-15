from django.test import TestCase
import jsonpickle
    


class NewsViewTest(TestCase):
    def test_forHomePage(self):
        response=self.client.get('/news')
        self.assertEqual(response.status_code,200)
        response=self.client.get('/news',{'next':''})
        self.assertEqual(response.status_code,200)
        self.assertGreaterEqual(len(response.context['articles']),1)
        response=self.client.get('/news',{'prev':''})
        self.assertEqual(response.status_code,200)
        self.assertGreaterEqual(len(response.context['articles']),1)
        
    def test2(self):
        response=self.client.get('/news',{'q':'Stack Overflow'})
        self.assertEqual(response.status_code,200)
        
    def test3(self):
        self.client.get('/news')
        prev_pref_body=jsonpickle.decode(self.client.session['pref'])['body']
        self.client.get('/news',{'next':''})
        self.assertEqual(jsonpickle.decode(self.client.session['pref'])['body'],prev_pref_body)
        
        

        
        

    
    
    