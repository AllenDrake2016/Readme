# name: Zihang Huang
# description: A Ball Class, inherits from Shape
# The Ball class keeps track of position, diameter, speed, and going_up values for a Ball

from Shape import *

class Ball(Shape):

    # initialization method
    # x -- x position of upper left corner of ball
    # y -- y poisitoin of upper left corner of ball
    # canvas -- window canvas, part of tkinter
    # color -- string; color of ball to be drawn
    # width -- width of paddle
    # height -- height of paddle
    def __init__(self, x, y, color, canvas, diameter):
        Shape.__init__(self, x, y, color, canvas)
        self.__diameter = diameter
        self.__going_up = True
        self.__going_left = True
        self.__speed = 3

    def set_diameter(self, diameter):
        self.__diameter = diameter

    def get_diameter(self):
        return self.__diameter

    def set_speed(self, speed):
        self.__speed = speed

    # bounce_vertical
    # ball changes direction up vs. down
    def bounce_vertical(self):
        if self.__going_up == True:
            self.__going_up = False
        else:
            self.__going_up = True

    def get_going_up(self):
        return self.__going_up

    def set_speed(self, speed):
        self.__speed = speed

    # move
    # ball values for x and y update according to speed
    def move(self):
        # move ball up or down
        if self.__going_up == True:
            self.set_y(self.get_y() - self.__speed)
        else:
            self.set_y(self.get_y() + self.__speed)

        # move ball left or right
        if self.__going_left == True:
            self.set_x(self.get_x() - self.__speed)
        else:
            self.set_x(self.get_x() + self.__speed)

        # make ball bounce vertically
        if self.get_y() + self.__diameter > self.get_canvas().winfo_height():
            self.__going_up = True

        if self.get_y() < 0:
            self.__going_up = False


        # make ball bounce horizontally
        if self.get_x() + self.__diameter > self.get_canvas().winfo_width():
            self.__going_left = True

        if self.get_x() < 0:
            self.__going_left = False


    # draw
    # draw the ball the appropriate color on the canvas
    def draw(self):
        self.get_canvas().delete("ball")
        self.get_canvas().create_oval(self.get_x(), self.get_y(),
                                self.get_x() + self.__diameter, self.get_y() + self.__diameter,
                                fill = self.get_color(), tags = "ball")


