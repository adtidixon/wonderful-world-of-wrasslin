from custom_actors import Actor2

WIDTH = 600
HEIGHT = 600

SPEED = 5

ring=Actor ('ring')
ring.pos=(300,300)

wrassler=Actor2('wrassler')
wrassler.pos=(165,165)
wrassler.hdir=0
wrassler.vdir=0

bad_wrassler=Actor2('bad_wrassler')
bad_wrassler.pos=(435,435)
bad_wrassler.angle=135
bad_wrassler.hdir=0
bad_wrassler.vdir=0

DIRS = {
    (0, 1): -90,#'UP',
    (0, -1): 90, #'DOWN',
    (-1, 0): 180, #'LEFT',
    (-1, 1): -135, #'TOPLEFT',
    (-1, -1): 135, #'BOTTOMLEFT',
    (1, 0): 0, #'RIGHT',
    (1, 1): -45, #'TOPRIGHT',
    (1, -1): 45, #'BOTTOMRIGHT',
}

wall = (120,480)

def update():
    pos = wrassler.pos


    new_pos = (pos[0]+wrassler.hdir*SPEED, pos[1]+ wrassler.vdir*SPEED)

    if new_pos[0] >= wall[0] and new_pos[0] <= wall[1] and new_pos[1] >= wall[0] and new_pos[1] <= wall[1]:
        wrassler.pos = new_pos

    pos = bad_wrassler.pos

    new_pos = (pos[0] + bad_wrassler.hdir * SPEED, pos[1] + bad_wrassler.vdir * SPEED)
    bad_wrassler.pos = new_pos

def draw():
    screen.clear()
    screen.fill((255,255,255))
    ring.draw()
    wrassler.draw()
    bad_wrassler.draw()

def rotate_wrassler():
    wrassler_dir = (wrassler.hdir, wrassler.vdir)
    if wrassler_dir != (0, 0):
        wrassler.angle = DIRS[wrassler_dir]

def on_key_down(key):
    if key == keys.LEFT:
        wrassler.hdir += -1
    elif key == keys.RIGHT:
        wrassler.hdir += 1
    if key == keys.UP:
        wrassler.vdir += -1
    elif key == keys.DOWN:
        wrassler.vdir += 1

    rotate_wrassler()

    if key == keys.SPACE:
        cankick = wrassler.colliderect(bad_wrassler)
        if cankick:
            bad_wrassler.hdir = wrassler.hdir
            bad_wrassler.vdir = wrassler.vdir


def on_key_up(key):
    if key == keys.LEFT:
        wrassler.hdir -= -1
    elif key == keys.RIGHT:
        wrassler.hdir -= 1
    if key == keys.UP:
        wrassler.vdir -= -1
    elif key == keys.DOWN:
        wrassler.vdir -= 1
    rotate_wrassler()