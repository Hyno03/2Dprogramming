from pico2d import load_image, clear_canvas, update_canvas, get_events,SDL_KEYDOWN, SDLK_ESCAPE, SDL_QUIT

import game_framework

def init():
    global image

    image = load_image('title.png')
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_OUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
    pass