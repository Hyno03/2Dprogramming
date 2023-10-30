import pico2d
from pico2d import clear_canvas, update_canvas, get_events,SDL_KEYDOWN,SDLK_ESCAPE,SDLK_SPACE, SDL_QUIT

import game_world
import game_framework
import play_mode
from pannel import Pannel

def init():
    global pannel

    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    global pannel

    game_world.remove_object(pannel)
    pass

def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_mode()
                case pico2d.SDLK_0:
                    play_mode.boy.item = None
                    game_framework.pop_mode()
                case pico2d.SDLK_1:
                    play_mode.boy.item = 'Ball'
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.item = 'BigBall'
                    game_framework.pop_mode()