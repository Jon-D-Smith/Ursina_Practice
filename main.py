from ursina import *

app = Ursina()

window.title = 'Test game'                
window.borderless = False               
window.fullscreen = True              
window.exit_button.visible = True     
window.fps_counter.enabled = True 

player = Entity(model="cube", color= color.red, scale_y = 2)
floor = Entity(model='quad', color=color.orange, position=(0,0,1), scale=1.5, rotation=(0,0,45), texture='brick')

def update():
    player.x += held_keys['d'] * (5 * time.dt)
    player.x -= held_keys['a'] * (5 * time.dt)
    player.y += held_keys['w'] * (5 * time.dt)
    player.y -= held_keys['s'] * (5 * time.dt)
    player.z += held_keys['q'] * (5 * time.dt)
    player.z -= held_keys['e'] * (5 * time.dt)
    camera.position = (player.x, player.y +2 ,player.z - 10) 

    
def input(key):
    if key == 'space':
        player.y += 3
        invoke(setattr, player, 'y', player.y-3, delay=.2)
            
            


app.run()