from kivy.app import App
from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from random import random
from kivy.properties import BooleanProperty


class Foundation1(Widget):
    start_x = 20
    start_y = 20
    rad = 60
    inc_pt = [2, 2]  # (magnitude) [x1, y1] ; increment x by 'x1' and y by 'y1' values
    vector1 = [1, 1]  # decides (direction) [x', y'], -1 means subtract, 1 means add
    win_size = Window.size
    disable_state = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0)
            self.el = Ellipse(pos=(self.start_x, self.start_y), size=(self.rad, self.rad))

    def direction(self, val_x, val_y):
        """
        Takes first position (old) and changes to make it move (new)
        old point was [val_x, val_y]
        new point is [(val_x + inc_pt[0]*vector1[0]), (val_y + inc_pt[1]*vector1[1])]
        :param val_x: x position at time 0
        :param val_y: y position at time 0
        :return: nothing, dos changes with val_x and val_y
        """
        random_x = int(random()*5)
        random_y = int(random()*5)

        # conditions decide direction and edit vactor1
        if val_x + self.rad >= self.win_size[0]:  # touches right vertical wall
            self.vector1[0] = -1
            self.inc_pt = [random_x, random_y]
            print(f"[inc_pt]: {self.inc_pt[0]}, {self.inc_pt[1]}")
        if val_y + self.rad >= self.win_size[1]:  # touches top wall
            self.vector1[1] = -1
            self.inc_pt = [random_x, random_y]
            print(f"[inc_pt]: {self.inc_pt[0]}, {self.inc_pt[1]}")
        if val_x <= 0:  # touches left vertical wall
            self.vector1[0] = 1
            self.inc_pt = [random_x, random_y]
            print(f"[inc_pt]: {self.inc_pt[0]}, {self.inc_pt[1]}")
        if val_y <= 0:  # touches bottom wall
            self.vector1[1] = 1
            self.inc_pt = [random_x, random_y]
            print(f"[inc_pt]: {self.inc_pt[0]}, {self.inc_pt[1]}")

        val_x += self.inc_pt[0]*self.vector1[0]
        val_y += self.inc_pt[1]*self.vector1[1]
        return [val_x, val_y]

    def anim1(self, dt):
        # Direction giving / next point -->
        self.start_x, self.start_y = self.direction(self.start_x, self.start_y)
        self.el.pos = (self.start_x, self.start_y)

    def repeater(self):
        self.disable_state = True
        Clock.schedule_interval(self.anim1, 0.05)

    def end_anim(self):
        exit()


class AutoBallApp(App):
    pass


AutoBallApp().run()
