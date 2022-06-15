from fileinput import close
import kivy
from kivymd.app import MDApp
from kivy.core.window import Window 
from kivy.lang import Builder 
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
Window.size=(300,450)
KV="""
Screen:
    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint:{"center_x": 0.5, "center_y": 0.5}
        elevation:10
        padding:65
        spacing:35
        orientation:'vertical'
        MDIcon:
            icon:'account'
            icon_color: 0, 0, 0, 0
            haling:'center'
            font_size:180
        MDTextFieldRound:
            id:user
            icon_left:"account-check"
            hint_text:"Usuario"
            foreground_color:1, 0, 1, 1
            size_hint_x: None
            width:220
            font_size:20
            pos_hint:{"center_x":0.5}
        MDTextFieldRound:
            id: password
            icon_left:"key-variant"
            hint_text:"Contraseña"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width:220
            font_size:20
            pos_hint: {"center_x":0.5}
            password: True
        MDFillRoundFlatButton:
            text: "LOGIN"
            font_size:15
            pos_hint: {"center_x":0.5}
            on_press:app.login()
"""

class LoginApp(MDApp):
    dialog:None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette ='Indigo'
        self.theme_cls.accent_palette = 'Blue'

        return Builder.load_string(KV)
    
    def login(self):
        if self.root.ids.user.text == 'admin' and self.root.ids.password.text == '123':
            if not self.dialog:
                self.dialog = MDDialog(
                    title='Login', 
                    text= f"Bienvenido {self.root.ids.user.text}!",
                    buttons=[
                        MDFlatButton(
                            text="Ok", text_color=self.theme_cls.accent_color,
                            on_release=self-close 
                        )
                    ]
                )
                self.dialog.open()

    def close (self):
        self.dialog.dismiss()


LoginApp().run()
