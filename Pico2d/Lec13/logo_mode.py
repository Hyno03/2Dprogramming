from pico2d import load_image, clear_canvas, update_canvas, get_events,get_time
import game_framework

def init():
    global image
    global running
    global logo_start_time

    image = load_image('tuk_credit.png')
    running = True
    logo_start_time = get_time()
    pass


def finish():
    pass


def update():
    global running

    if get_time() - logo_start_time >= 2.0:
        running = False
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass