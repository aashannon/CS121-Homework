#Aaron Shanon
#CS 121 T/Th




import turtle
from turtle import *
from time import sleep


class MyDrawing(object):
    """This is the MyDrawing Class"""
    """This will hold all the art building functions and definitions"""
    def __init__(self):

        width(1)
        speed('fastest')
        

    def drawSquare(self,colors):
        """This function will be solely for creating a square 
        and filling it with the color passed to it"""
        side = 10
        color(colors)
        begin_fill()
        for i in range(4):
            forward(side)
            right(90)
        end_fill()
        forward(side)

    def nextRow(self):
        """This function will move the turtle back to the beginning
        and up to start the next row"""
        side = 10
        numSquares = 30
        penup()
        backward(numSquares * side)
        left(90)
        forward(side)
        right(90)
        pendown()

    def drawRow(self,colors, numbers):
        """This function will draw the row based on the length of colors[]
        and the number of squares each colors takes up, the calls nextRow()"""
        for j in range(len(colors)):
            for k in range(numbers[j]):
                self.drawSquare(colors[j])
        self.nextRow()

    def drawGhast(self):
        """This function holds all the specific colors and number of squares 
        to be used on each row"""
        tracer(0,0)

        purp1 = '#9508FF'
        purp2 = '#B54CFE'
        purp3 = '#BE71FD'
        purp4 = '#6202A7'
        gray1 = '#DCDCDC'
        gray2 = '#808080'
        gray3 = '#2C2B2C'
        pink1 = '#FF69B4'
        pink2 = '#C71585'
        oran1 = '#DB5000'
        red01 = '#9F0901'

        colors = ['white',purp1,'white',purp1,'white']
        numbers = [11,2,1,3,13]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,purp1,'white']
        numbers = [8,3,2,1,3,2,11]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,purp2,purp1,'white']
        numbers = [7,1,4,4,3,1,10]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,purp3,purp2,purp1,'white',purp1,'white']
        numbers = [6,1,3,5,1,1,2,1,3,2,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,gray1,gray3,purp2,purp1,'white',purp1,purp3,purp1,'white']
        numbers = [5,1,3,3,3,1,1,3,1,2,1,1,1,4]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,pink1,'white',purp4,gray3,purp2,purp1,'white',purp1,purp2,purp1,'white']
        numbers = [5,1,4,2,3,1,1,1,2,1,2,1,1,1,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,pink2,purp4,pink2,purp4,gray3,purp2,purp1,purp2,purp1,'white']
        numbers = [5,1,3,1,3,3,1,1,1,2,2,1,1,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,purp2,gray3,purp4,oran1,'white',purp4,gray3,purp2,purp1,'white']
        numbers = [2,2,1,1,2,1,3,1,3,3,1,5,1,4]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,gray3,purp4,red01,'white',gray3,'white',gray1,red01,purp4,gray3,purp2,purp1,'white']
        numbers = [2,1,1,2,2,1,2,1,1,1,2,1,1,1,1,6,2,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,gray3,'white',purp4,'white',gray3,'white',gray2,red01,purp4,gray3,purp2,purp3,purp1,'white']
        numbers = [3,1,2,1,1,1,3,1,1,3,1,1,1,1,1,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',gray3,'white',gray3,'white',purp4,red01,purp4,gray1,'white',gray1,oran1,purp4,gray3,purp2,purp3,purp1,'white']
        numbers = [6,1,1,1,1,1,1,1,2,2,1,1,1,1,1,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',gray3,'white',gray3,red01,purp4,oran1,purp4,gray2,gray1,purp4,gray3,purp3,purp1,'white']
        numbers = [6,1,1,1,1,1,1,3,1,2,2,1,6,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,gray3,'white',gray1,oran1,purp4,gray2,purp4,gray3,purp3,purp1,purp3,purp1,'white']
        numbers = [3,3,1,1,1,1,7,1,2,1,2,2,2,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,'white',gray2,purp4,gray3,purp3,purp1,'white',purp1,'white']
        numbers = [2,1,3,1,1,1,10,1,2,2,1,2,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,gray1,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [2,1,3,1,1,1,10,1,2,1,7]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,purp3,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [2,1,2,2,1,1,1,8,1,3,1,7]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp3,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [3,1,6,2,4,2,5,3,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp3,purp2,gray3,purp2,purp3,purp2,purp3,purp1,'white']
        numbers = [3,1,1,3,2,2,4,3,1,1,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,purp2,purp3,purp2,purp3,purp2,purp1,purp2,purp3,purp1,'white']
        numbers = [4,2,1,1,1,2,1,3,2,2,3,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,purp1,'white',purp1,purp2,purp3,purp1,'white']
        numbers = [7,1,4,3,1,1,2,1,3,4,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white',purp2,purp1,'white',purp1,purp2,purp3,purp1,'white']
        numbers = [7,1,4,1,2,2,1,2,1,4,2,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white',purp1,purp2,purp1,'white',purp1,purp2,purp1,'white']
        numbers = [7,3,1,2,1,1,2,1,2,1,5,2,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,'white',purp1,purp2,purp1,'white']
        numbers = [9,3,2,4,2,1,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white']
        numbers = [21,1,4,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white']
        numbers = [22,4,4]
        self.drawRow(colors,numbers)

        update()


    def drawHaunter(self):
        """This holds all the specific colors, number of 'pixels', and passes them to drawRow"""
        tracer(0,0)

        purp1 = '#65339C'
        purp2 = '#7C64A0'
        gray1 = '#5C5C5C'
        pink1 = '#F4CECF'
        pink2 = '#EF9D9B'

        colors = ['white','black','white','black','white']
        numbers = [21,2,2,1,4]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'black','white','black',purp1,'black','white']
        numbers = [20,1,1,1,1,1,1,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black',gray1,purp1,'black',purp1,purp2,'black','white']
        numbers = [19,1,1,2,1,1,1,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,gray1,purp2,gray1,purp2,'black','white']
        numbers = [18,1,1,1,2,1,2,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp2,gray1,purp2,'black','white']
        numbers = [16,3,2,1,4,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black','white','black',purp1,'black',purp2,'black','white']
        numbers = [6,1,7,2,3,1,5,3,2]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'black','white','black',purp1,gray1,purp1,'black',purp2,'black',purp1,'black','white']
        numbers = [5,1,1,1,5,1,1,3,2,2,2,1,3,1,1]
        self.drawRow(colors,numbers)

        colors = ['white','black','white','black',purp1,'black','white','black',gray1,pink1,gray1,purp1,'black',purp1,'black']
        numbers = [1,2,1,1,2,1,4,1,2,3,1,3,2,5,1]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'black',purp1,'black','white','black',gray1,pink2,pink1,pink2,gray1,purp1,'black','white']
        numbers = [1,1,1,2,3,1,2,1,1,1,3,2,1,7,2,1]
        self.drawRow(colors,numbers)

        colors = ['black',purp1,gray1,purp2,purp1,gray1,purp2,purp1,'black','white','black',pink2,gray1,pink2,gray1,pink2,gray1,purp1,gray1,'black','white']
        numbers = [1,1,1,1,1,1,2,1,1,2,1,1,1,2,1,2,1,3,2,1,3]
        self.drawRow(colors,numbers)

        colors = ['black',purp1,gray1,purp2,'black','white','black',pink2,gray1,purp1,gray1,purp1,gray1,purp1,'black','white']
        numbers = [1,1,1,6,1,1,1,1,1,1,2,1,3,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,gray1,purp2,'black','white','black',purp1,gray1,purp1,'white',purp1,gray1,purp1,'black','white']
        numbers = [1,1,1,1,3,2,1,1,1,1,4,3,1,1,3,1,4]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp2,'black','white','black',purp1,gray1,'white','black','white',purp1,gray1,'black','white']
        numbers = [2,2,2,1,2,1,4,1,1,1,3,4,2,1,2]
        self.drawRow(colors,numbers)

        colors = ['white','black','white','black',purp1,purp2,purp1,'black',gray1,'white',purp1,'black','white']
        numbers = [4,2,3,1,3,1,2,1,1,2,7,2,1]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'black',purp2,gray1,purp1,gray1,purp1,'black']
        numbers = [8,1,2,1,6,2,4,1,4,1]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'white','black',purp2,gray1,purp2,gray1,'black','white']
        numbers = [8,1,1,1,1,8,1,4,1,3,1]
        self.drawRow(colors,numbers)

        colors = ['white','black','white',purp2,purp1,'black','white']
        numbers = [9,1,1,10,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white','black',gray1,'white',purp2,purp1,purp2,purp1,'black','white']
        numbers = [8,1,1,1,3,3,7,3,1,2]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,gray1,purp2,purp1,purp2,purp1,'black','white']
        numbers = [8,1,1,1,3,6,6,2,1,1]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,gray1,purp2,purp1,purp2,'black',purp2,purp1,'black']
        numbers = [7,1,2,1,2,6,2,5,2,1,1]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp1,'black',purp2,purp1,'black','white','black']
        numbers = [7,1,1,2,2,6,2,5,4]
        self.drawRow(colors,numbers)

        colors = ['white','black','white','black',purp2,purp1,'black','white']
        numbers = [7,2,2,1,2,1,4,11]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp2,purp1,'black','white']
        numbers = [11,1,2,1,1,14]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp2,'black','white']
        numbers = [12,1,1,1,15]
        self.drawRow(colors,numbers)

        colors = ['white','black',purp2,'black','white']
        numbers = [12,1,1,1,15]
        self.drawRow(colors,numbers)

        colors = ['white','black','white']
        numbers = [13,1,16]
        self.drawRow(colors,numbers)

        update()


    def ghastEvo(self):
        """This function holds all the specific colors and number of squares 
        to be used on each row for the evolution"""
        tracer(0,0)

        purp1 = '#EACEFF'
        purp2 = '#F0DBFF'
        purp3 = '#F2E2FE'
        purp4 = '#DABEED'
        gray1 = '#F8F8F8'
        gray2 = '#E6E6E6'
        gray3 = '#D5D4D5'
        pink1 = '#FFE1F0'
        pink2 = '#F4C8E4'
        oran1 = '#F8D8C6'
        red01 = '#ECBFBD'

        colors = ['white',purp1,'white',purp1,'white']
        numbers = [11,2,1,3,13]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,purp1,'white']
        numbers = [8,3,2,1,3,2,11]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,purp2,purp1,'white']
        numbers = [7,1,4,4,3,1,10]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,purp3,purp2,purp1,'white',purp1,'white']
        numbers = [6,1,3,5,1,1,2,1,3,2,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,gray1,gray3,purp2,purp1,'white',purp1,purp3,purp1,'white']
        numbers = [5,1,3,3,3,1,1,3,1,2,1,1,1,4]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,pink1,'white',purp4,gray3,purp2,purp1,'white',purp1,purp2,purp1,'white']
        numbers = [5,1,4,2,3,1,1,1,2,1,2,1,1,1,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,pink2,purp4,pink2,purp4,gray3,purp2,purp1,purp2,purp1,'white']
        numbers = [5,1,3,1,3,3,1,1,1,2,2,1,1,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,purp2,gray3,purp4,oran1,'white',purp4,gray3,purp2,purp1,'white']
        numbers = [2,2,1,1,2,1,3,1,3,3,1,5,1,4]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,gray3,purp4,red01,'white',gray3,'white',gray1,red01,purp4,gray3,purp2,purp1,'white']
        numbers = [2,1,1,2,2,1,2,1,1,1,2,1,1,1,1,6,2,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,gray3,'white',purp4,'white',gray3,'white',gray2,red01,purp4,gray3,purp2,purp3,purp1,'white']
        numbers = [3,1,2,1,1,1,3,1,1,3,1,1,1,1,1,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',gray3,'white',gray3,'white',purp4,red01,purp4,gray1,'white',gray1,oran1,purp4,gray3,purp2,purp3,purp1,'white']
        numbers = [6,1,1,1,1,1,1,1,2,2,1,1,1,1,1,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',gray3,'white',gray3,red01,purp4,oran1,purp4,gray2,gray1,purp4,gray3,purp3,purp1,'white']
        numbers = [6,1,1,1,1,1,1,3,1,2,2,1,6,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,gray3,'white',gray1,oran1,purp4,gray2,purp4,gray3,purp3,purp1,purp3,purp1,'white']
        numbers = [3,3,1,1,1,1,7,1,2,1,2,2,2,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,'white',gray2,purp4,gray3,purp3,purp1,'white',purp1,'white']
        numbers = [2,1,3,1,1,1,10,1,2,2,1,2,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,gray3,gray1,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [2,1,3,1,1,1,10,1,2,1,7]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp3,gray3,purp3,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [2,1,2,2,1,1,1,8,1,3,1,7]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp3,gray3,purp4,gray3,purp3,purp1,'white']
        numbers = [3,1,6,2,4,2,5,3,5]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp3,purp2,gray3,purp2,purp3,purp2,purp3,purp1,'white']
        numbers = [3,1,1,3,2,2,4,3,1,1,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,purp2,purp3,purp2,purp3,purp2,purp1,purp2,purp3,purp1,'white']
        numbers = [4,2,1,1,1,2,1,3,2,2,3,5,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,purp2,purp1,'white',purp1,purp2,purp3,purp1,'white']
        numbers = [7,1,4,3,1,1,2,1,3,4,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white',purp2,purp1,'white',purp1,purp2,purp3,purp1,'white']
        numbers = [7,1,4,1,2,2,1,2,1,4,2,1,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white',purp1,purp2,purp1,'white',purp1,purp2,purp1,'white']
        numbers = [7,3,1,2,1,1,2,1,2,1,5,2,2]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white',purp1,'white',purp1,purp2,purp1,'white']
        numbers = [9,3,2,4,2,1,5,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,purp2,purp1,'white']
        numbers = [21,1,4,1,3]
        self.drawRow(colors,numbers)

        colors = ['white',purp1,'white']
        numbers = [22,4,4]
        self.drawRow(colors,numbers)

        update()


    def moveArt(self,x,y):
        """This function simply allows the picture to be moved around
        the screen based on the x and y coordinates passed to it"""
        pu()
        goto(x,y)
        pd()

    def resetArt(self,x,y):
        """This just erases the sprite"""
        sleep(0.1)
        clear()

    def animateArt(self, poke):
        """This function is meant to move the picture
        up and down, as if to be animated."""
        n = 0
        x = -125
        count = 0
        for i in range(0,10):
            if count <= 4:
                y = -100 - n
                self.moveArt(x,y)
                if poke == 'g':
                    self.drawGhast()
                elif poke == 'h':
                    self.drawHaunter()
                self.resetArt(x,y)
                n+=10
                count+=1
            elif count <= 8 or count > 4:
                y = -100 - n
                self.moveArt(x,y)
                if poke == 'g':
                    self.drawGhast()
                elif poke == 'h':
                    self.drawHaunter()
                self.resetArt(x,y)
                n-=10
                count+=1

    def evolvePoke(self):
        """This replaces the image with another version then calls the drawHaunter function"""
        y = -100
        x = -125
        count = 0
        for i in range(0,6):
            if count <= 4:
                self.moveArt(x,y)
                self.drawGhast()
                self.resetArt(x,y)
                self.moveArt(x,y)
                self.ghastEvo()
                self.resetArt(x,y)
                count+=1
            elif count <= 8 or count > 4:
                self.moveArt(x,y)
                self.drawGhast()
                self.resetArt(x,y)
                self.moveArt(x,y)
                self.ghastEvo()
                self.resetArt(x,y)
                count+=1

        self.moveArt(x,y)
        self.drawHaunter()

        sleep(0.1)

        self.resetArt(x,y)
        self.animateArt('h')

        self.moveArt(x,y)
        self.resetArt(x,y)
        self.drawHaunter()


            
def main():
    myArt = MyDrawing()
    myArt.animateArt('g')
    myArt.evolvePoke()
    turtle.getcanvas().postscript(file="Evolution.ps", colormode='color')
    done()


if __name__ == '__main__':
    main()