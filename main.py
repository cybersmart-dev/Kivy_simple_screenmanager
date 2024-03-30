
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import sys

# kivy app screenmanager

Builder.load_string("""

<SM>
    Home:
        name:"home"
        
    Screeb2:
        name:"screen2"

<Screeb2>
    BoxLayout:
        orientation:'vertical'
        
        Button:
            text:"exit to app"
            on_press:app.quit(self)
            
        Button:
            text:"Go To Home"
            on_press:app.home(self)
<Home>
    BoxLayout:
        orientation:'vertical'
        
        Button:
            text:"exit to app"
            on_press:app.quit(self)
        Button:
            text:"Go To Screen2"
            on_press:app.screen2(self)
        
""")

class SM(ScreenManager):
    pass
    
class Screeb2(Screen):
    pass
       
class Home(Screen):
    pass
        
class myapp(App):
    def build(self):
        return SM()
        
    def quit(self, btn):
        sys.exit()
    
    def home(self, btn):
        self.root.current = "home" 
        
    def screen2(self, btn):
        self.root.current = "screen2"
        
myapp().run()
