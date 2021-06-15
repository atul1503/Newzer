from django.test import TestCase

    


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
        

        

        
        

    
    
    