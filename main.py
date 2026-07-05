from kivy.app import App
from kivy.uix.vboxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from jnius import autoclass

class TarayiciUygulamasi(App):
    def build(self):
        self.ana_duzen = BoxLayout(orientation='vertical')
        ust_menu = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        
        self.adres_cubugu = TextInput(text='https://www.google.com', multiline=False)
        ust_menu.add_widget(self.adres_cubugu)
        
        git_butonu = Button(text='Git', size_hint_x=0.2)
        git_butonu.bind(on_press=self.web_sitesine_git)
        ust_menu.add_widget(git_butonu)
        
        self.ana_duzen.add_widget(ust_menu)
        
        Activity = autoclass('org.kivy.android.PythonActivity').mActivity
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        
        self.webview = WebView(Activity)
        self.webview.getSettings().setJavaScriptEnabled(True)
        self.webview.setWebViewClient(WebViewClient())
        
        self.webview.loadUrl(self.adres_cubugu.text)
        Activity.setContentView(self.webview)
        
        return self.ana_duzen

    def web_sitesine_git(self, instance):
        url = self.adres_cubugu.text
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
            self.adres_cubugu.text = url
        self.webview.loadUrl(url)

if __name__ == '__main__':
    TarayiciUygulamasi().run()

