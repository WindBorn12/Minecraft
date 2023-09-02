from ursina import *

app = Ursina()
class TestEntity(Entity):
    def __int__(self,model='cube'):
        super().__init__(
            model=model,
            color=color.white,
            texture='white_cube'
        )
class TestButton(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='grass',
            color=color.green,
            highlight_color=color.blue,
            pressed_color=color.red
        )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print("sol tikladi")


TestEnt = TestButton()


app.run()