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
sprite.set_size_percent(wu,150,150)
top1=sprite.get_top(leftupshelf)
top2=sprite.get_top(leftdownshelf)
top3=sprite.get_top(rightupshelf)
top4=sprite.get_top(rightdownshelf)
sprite.move_bottom_to(leftupchicken,top1)
sprite.move_bottom_to(leftdownchicken,top2)
sprite.move_bottom_to(rightupchicken,top3)
sprite.move_bottom_to(rightdownchicken,top4)
a=None

egglist=[]
egglist2=[]
egglist3=[]
egglist4=[]
def prizemli_na_polky(e,s):
    shelfright=sprite.get_right(s)
    egg_left=sprite.get_left(e)
    if egg_left+4>shelfright:
        return False

    while not sprite.is_collide_sprite(e,s):
        sprite.move(e,0,1)
    else:
        sprite.move(e,0,-1)
    return True



def move_egg(egg,shelf):

    if prizemli_na_polky(egg, shelf):
        sprite.move(egg, 5, 0)
        ang = sprite.get_angle(egg)
        sprite.set_angle(egg, ang + 15)
        prizemli_na_polky(egg, shelf)
    else:
        sprite.move(egg, 0, 5)


@wrap.always(200)
def eggmover ():
    global egg,egg2
    for egg in egglist:
        move_egg(egg,leftupshelf)
    for egg in egglist2:
        move_egg(egg, leftdownshelf)
    for egg in egglist3:
        move_egg2(egg, rightupshelf)
    for egg in egglist4:
        move_egg2(egg, rightdownshelf)


def prizemli_na_polky2(e,s):
    shelfleft=sprite.get_left(s)
    egg_right=sprite.get_right(e)
    if egg_right-4<shelfleft:
        return False

    while not sprite.is_collide_sprite(e,s):
        sprite.move(e,0,1)
    else:
        sprite.move(e,0,-1)
    return True

def move_egg2(egg,shelf):

    if prizemli_na_polky2(egg, shelf):
        sprite.move(egg, -5, 0)
        ang = sprite.get_angle(egg)
        sprite.set_angle(egg, ang - 15)
        prizemli_na_polky(egg, shelf)
    else:
        sprite.move(egg, 0, 5)


@wrap.always(2000)
def eggspawn():

    lists=random.choice([egglist,egglist2,egglist3,egglist4])
    if lists is egglist or lists is egglist2:
        x,y=[5,5]
    else:
        x,y=[635,5]
    egg = sprite.add("egg", x, y, "egg")
    lists.append(egg)





















