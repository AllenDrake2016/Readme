# author: Zihang Huang
# date:
# description: The Driver class for a Pong game
# proposed points (out of 20): 18, I believe I can get 18. I meet all the requirement except
#                                           "Implement an original game (other than Pong)."


from Paddle import *
from Ball import *
from tkinter import *
import winsound

class Pong:
    def __init__(self):
        window = Tk()
        window.title("Pong") # Set a title

        # set callback routine when mouse is moved
        window.bind("<Motion>", self.callback)

        # establish the canvas
        self.__width = 400 # Width of the self.canvas
        self.__height = 400 # Width of the self.canvas
        self.__canvas = Canvas(window, bg = "white",
            width = self.__width, height = self.__height)
        self.__canvas.pack()
        self.__color="red"

        # create ball and paddle objects
        self.__ball = Ball(130,40,self.__color, self.__canvas, 30)
        self.__paddle = Paddle(380,380,"black", self.__canvas, 100, 20)

        # start the animation loop
        self.animate()

    # callback method
    # when mouse is moved, get the x-position of the mouse
    # set it to be the paddle x position
    def callback(self, event):
        x = event.x
        self.__paddle.set_x(x)

    # animation
    def animate(self):
        score=0
        while True:

            self.__canvas.after(20) # Speed
            self.__canvas.update() # Update self.canvas


            # colision detection code will go here
            if self.__ball.get_going_up()==False and \
                self.__ball.get_x()+self.__ball.get_diameter()>self.__paddle.get_x() and \
                self.__ball.get_x()<self.__paddle.get_x() + self.__paddle.get_width() and \
                self.__ball.get_y()+self.__ball.get_diameter()>self.__paddle.get_y():
                self.__canvas.delete("gameOver")
                self.__ball.bounce_vertical()
                score += 1
                self.__canvas.create_text(250, 20, text = ("Scored "+str(score)), font=("Helvetica", 12, "bold"), fill = "red", tags = ("gameOver"))
                winsound.PlaySound('boing.wav',winsound.SND_ASYNC)

            if score % 2 == 0:
                self.__ball.set_color("blue")
            else:
                self.__ball.set_color("red")


            if self.__ball.get_y()+ self.__ball.get_diameter() == 400:
                self.__ball.set_speed(0)
                self.__canvas.delete("gameOver")
                self.__canvas.create_text(250, 20, text = ("Game Over! You scored "+str(score)), font=("Helvetica", 12, "bold"), fill = "red", tags = ("gameOver"))


            # move the ball and draw the objects
            self.__ball.move()
            self.__ball.draw()
            self.__paddle.draw()




Pong()

