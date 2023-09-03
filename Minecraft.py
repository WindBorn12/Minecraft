from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

chosenBlock = 1

game_area = 20

txt = Text(text="")




def update():
    global chosenBlock
    global txt
    if held_keys["1"]:
        chosenBlock = 1
        destroy(txt)
        txt = Text(text="white block selected",y=.5,x=-.1)
    if held_keys["2"]:
        chosenBlock = 2
        destroy(txt)
        txt = Text(text="grass selected",y=.5,x=-.1)
    if held_keys["3"]:
        chosenBlock = 3
        destroy(txt)
        txt = Text(text="wood selected",y=.5,x=-.1)
    if held_keys["4"]:
        chosenBlock = 4
        destroy(txt)
        txt = Text(text="stone selected",y=.5,x=-.1)

class Block(Button):
    def __init__(self, position=(0,0,0), texture='grass'):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = texture,
            color = color.white,
            origin_y = .5,
            highlight_color = color.lime,
        )
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if chosenBlock == 1:
                    block = Block(position=self.position + mouse.normal,texture='white_cube')
                if chosenBlock == 2:
                    block = Block(position=self.position + mouse.normal, texture='grass')
                if chosenBlock == 3:
                    block = Block(position=self.position + mouse.normal, texture=load_texture('wood.png'))
                if chosenBlock == 4:
                    block = Block(position=self.position + mouse.normal, texture=load_texture('stone.png'))
            if key == 'left mouse down':
                destroy(self)




app = Ursina(borderless=False)


player=FirstPersonController()

for x in range(game_area):
    for y in range(game_area):
        block = Block(position=(x,0,y),texture='grass')



window.fullscreen_resolution = (1920, 1080)
window.fullscreen = True
app.run()