from pico2d import open_canvas, delay, close_canvas

import logo_mode

open_canvas()
logo_mode.init()
# game loop
while logo_mode.running:
    logo_mode.handle_events()
    logo_mode.update()
    logo_mode.draw()
    delay(0.01)

logo_mode.finish()
close_canvas()