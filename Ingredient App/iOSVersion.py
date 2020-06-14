import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

#Class for layout
class MyBox(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBox, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='horizontal')

        self.vegan_button = Button(text="Vegan", background_color="red")
        self.add_widget(self.vegan_button,index=3)
        self.vegan_button.bind(on_press=self.ve_pressed)
        
        self.keto_button = Button(text="Keto")
        self.add_widget(self.keto_button,index=2)
        self.keto_button.bind(on_press=self.k_pressed)
        
        self.vege_button = Button(text="Vegetarian")
        self.add_widget(self.vege_button,index=1)
        self.vege_button.bind(on_press=self.v_pressed)
        
        self.paleo_button = Button(text="Paleo")
        self.add_widget(self.paleo_button, index=0)
        self.paleo_button.bind(on_press=self.p_pressed)
        # self.chris = Button(text="Chris")
        #self.add_widget(Button(text="Chris"), index=4)
    
    def p_pressed(self, instance):
        print("Paleo")
    def v_pressed(self, instance):
        print("Vegentarian")
    def k_pressed(self, instance):
        print("Keto")
    def ve_pressed(self, instance):
        print("Vegan")
    def c_pressed(self, instance):
        print("Chris")

#Class that puts all pieces together
class IngredientReplacer(App):
    def build(self):
        return MyBox()

if __name__ == "__main__":
    IngredientReplacer().run()