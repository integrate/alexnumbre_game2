import time,wrap,random
wrap.add_sprite_dir("mysprites")
from wrap import world,sprite
from random import randint

world.create_world(640,480)
world.set_back_color(0, 150, 150)
rightupchicken=sprite.add("chicken",637,104,"chicken")
rightdownchicken=sprite.add("chicken",637,226,"chicken")
leftupchicken=sprite.add("chicken",5,104,"chicken")
leftdownchicken=sprite.add("chicken",5,226,"chicken")
rightupshelf=sprite.add("shelf", 550,130,"shelf")
rightdownshelf=sprite.add("shelf", 550,250,"shelf")
leftupshelf=sprite.add("shelf", 90,130,"shelf")
leftdownshelf=sprite.add("shelf", 90,250,"shelf")
wu=sprite.add("woolfs",320,260,"woolfup")
sprite.set_reverse_x(leftupshelf,True)
sprite.set_reverse_x(leftdownshelf,True)
sprite.set_reverse_x(leftupchicken,True)
sprite.set_reverse_x(leftdownchicken,True)
sprite.set_size_percent(wu,30,30)
top1=sprite.get_top(leftupshelf)
top2=sprite.get_top(leftdownshelf)
top3=sprite.get_top(rightupshelf)
top4=sprite.get_top(rightdownshelf)
sprite.move_bottom_to(leftupchicken,top1)
sprite.move_bottom_to(leftdownchicken,top2)
sprite.move_bottom_to(rightupchicken,top3)
sprite.move_bottom_to(rightdownchicken,top4)
a=None
fall=0

def down():
    global fall
    fall = 0
    shelfright=sprite.get_right(leftupshelf)
    egg_left=sprite.get_left(egg)
    if egg_left+4>shelfright:
        fall=1
        return
    while not sprite.is_collide_sprite(egg,leftupshelf):
        sprite.move(egg,0,1)
    else:
        sprite.move(egg,0,-1)




#@wrap.always()
def eggf ():
    global a,egg
    a=randint(1,1)
    if a ==1:
        egg=sprite.add("egg",5,5,"egg")

@wrap.always(200)
def eggo ():
    global egg
    if a ==1 and fall==0:
        sprite.move(egg,5,0)
        ang = sprite.get_angle(egg)
        sprite.set_angle(egg,ang+15)
        down()
    else: sprite.move(egg,0,5)






eggf()




