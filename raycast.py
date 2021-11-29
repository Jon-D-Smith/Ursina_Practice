from ursina import *
app = Ursina()


class Player(Entity):

    def input(player, value):
        if value == "space" and player.jump_count < 2:
            player.jump_count += 1
            player.position += Vec3(0,player.jump_force,0) * 5 * time.dt


    def update(self):
        self.jump_count = 0
        self.jump_force = 30
        self.gravity =  -2.5

        if self.position.y > 0:
            self.position += Vec3(0,self.gravity,0) * 5 * time.dt

        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        camera.x = self.position.x
        camera.z = self.position.z - 20
        camera.rotation_x = mouse.position.x
        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt
       
    
                

Player(model='cube', origin_y=-.5, color=color.orange)
wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
wall_right = duplicate(wall_left, x=4)
camera.y = 2

app.run()