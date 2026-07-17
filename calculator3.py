from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
class Calculator(App):
    def build(self):
        layout=BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )
        self.display=TextInput(
            text="",
            readonly=True,
            font_size=40,
            multiline=False
        )
        button_layout=GridLayout(
            cols=5,
            spacing=10
        )
        buttons=[
            "7","8","9","Del","±",
            "4","5","6","×","÷",
            "1","2","3","-","%",
            "C","0",".","+","=",
            "History"
        ]
        for text in buttons:
            button=Button(
                text=text,
                font_size=30
            )
            button.bind(on_press=self.button_pressed)
            button_layout.add_widget(button)
        layout.add_widget(self.display)
        layout.add_widget(button_layout)
        self.history=[]
        self.just_calculated=False
        return layout
    def button_pressed(self,instance):
        if instance.text=="=":
            try:
                expression=self.display.text
                expression=expression.replace("×","*")
                expression=expression.replace("÷","/")
                answer=str(eval(expression))
                self.history.append(self.display.text+"="+answer)
                print(self.history)
                self.display.text=answer
                self.just_calculated=True
            except:
                self.display.text="Error"
        elif instance.text=="C":
            self.display.text=""
        elif instance.text=="Del":
            self.display.text=self.display.text[:-1]
        elif instance.text=="%":
            self.display.text=str(float(self.display.text)/100)
        elif instance.text=="±":
            if self.display.text!="":
                if self.display.text.startswith("-"):
                    self.display.text=self.display.text[1:]
                else: 
                    self.display.text="-"+self.display.text
        elif instance.text=="History":
            history_text="\n".join(self.history)
            popup=Popup(
                title="Calculation History",
                content=Label(text=history_text),
                size_hint=(0.8,0.8)
            )
            popup.open()    
        else:
            if self.display.text=="Error":
                self.display.text=""
            if  self.just_calculated and instance.text.isdigit():
                self.display.text=""
                self.just_calculated=False
            self.display.text+=instance.text
            if instance.text in["+","-","×","÷","%"]:
                self.just_calculated=False
Calculator().run()
