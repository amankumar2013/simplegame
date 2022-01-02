from ursina import *

window.borderless = False

app = Ursina()
def update():
    
    if held_keys['m']:
        camera.position += (0, time.dt, 0)
    if held_keys['n']:
        camera.position -= (0, time.dt, 0)
window.title = 'My Game'

square = Entity(model='quad', color=color.red, scale=(1,4), position=(5,1))

square2 = Entity(model='quad', texture='brick', scale=(1,4), position=(5,-5))
app.run()