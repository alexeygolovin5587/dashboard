import multiprocessing
import threading
import time
import sys
import cv2
from pyglet import font
from pyglet.gl import *
from pyglet.window import key
import cocos
from cocos.text import Label
from cocos.actions import *
from cocos import scene
from cocos.layer import Layer
from cocos.sprite import Sprite
from cocos.director import director
from cocos.text import Label
from pyglet.window.key import symbol_string
import logging


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if face_cascade.empty(): raise Exception("your face_cascade is empty. are you sure, the path is correct ?")

def WatchInit():
        
      while(video.isOpened()):
          
       #if frame is not None:
       a =int( WatchMe() or 0)
       print (a)
       sys.stdout.flush()
       cv2.waitKey(500)
      # if cv2.waitKey(1) & 0xFF == ord('q'):
       #if cv2.waitKey(500) :
          #video.release()
         # cv2.destroyAllWindows()
          #return a
         # break
     

def WatchMe():      
        ret, frame = video.read()
        if frame is not None: 
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
         
         for (x,y,w,h) in faces:
                                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)                               
                                t =(x+w)/2
                                v =(y+h)/2
                                #cv2.circle(frame, (t,v), 1, (0,0,255), thickness=1, lineType=8, shift=0)
                                roi_gray = gray[y:y+h, x:x+w]
                                roi_color = frame[y:y+h, x:x+w]
                                #eyes = eye_cascade.detectMultiScale(roi_gray)
                                #for (ex,ey,ew,eh) in eyes:
                                    #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                                #print (x,y,w,h)
                                #print (t,v)
                                cv2.imshow('Video', frame)
                                #cv2.waitKey(300)
                                return t


class InputExample(Layer):
    is_event_handler = True

    def __init__(self):
				super(InputExample, self).__init__()

				# Let's create a sprite this time instead of using Labels
				self.sprite = Sprite("emoticon.png")
				self.sprite.position = 320, 240

				# While we're at it let's make it fancy by having our sprite fade in
				self.sprite.opacity = 0
				self.add(self.sprite)
				self.sprite.do(FadeIn(2))

        # Remember that our layer is an event handler
        # This means that I don't need to add any calls to functions to execute the actions on those events

    # Let's start with that jump action
    # To start I need to overload the default click function
    def on_mouse_press(self, x, y, buttons, modifiers):
        # Remember that we said we only wanted to jump on left clicks
        # The number 1 represents left clicks in Cocos
        # You can test this by adding a print statement for the buttons input
        #if buttons == 1:
       if buttons == 1:
            # The Jump action requires 4 inputs
            # 1. How high on the Y axis the sprite should jump
            # 2. How far on the X axis the sprite should jump to
            # 3. How many times the sprite should jump
            # 4. How many seconds it should take for the action to complete
            self.sprite.do(Jump(50, 0, 1, 1))

            # Pretty easy, huh? Now let's do the movement

    # Once again we overload a default event handler
    def on_key_press(self, key, modifiers):
        # First I create a move action because we programmers are lazy and hate having to retype code!
        move_left = MoveBy((-50, 0), .5)

        # Here's where that Pyglet symbol_string() function comes in handy
        # Rather than having to interpret an inconsistent code, I can simply interpret the word LEFT and RIGHT
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        # Now I need to tell the layer what to do if the user inputs RIGHT
        if symbol_string(key) == "RIGHT":
            # This is a pretty awesome feature built into Cocos
            # I only wrote code for moving left, but I can use the Reverse() function instead of rewriting code
            # Reverse() simply tells Cocos to do the reverse action of whatever you pass into it.
            self.sprite.do(Reverse(move_left))


def func():
	while(1):
		print "pppp"

def cocos():
	#director.init()
	d=InputExample()
	director.run(scene.Scene(d))
	sys.stdout.flush()


#while(video.isOpened()):
#while 1 :
# From here the code is pretty typical for a Cocos2D application
# First I need to initialize the cocos director
# The director is the part of cocos that "directs" the scenes. Cocos is pretty partial to this type of film language

    
#director.init()
# Lastly I run the scene. This line of code is pretty long compared to the others, so I'll explain what each part does
# To begin I call the director's run function, which allows it to run the scene by placing layers within
#director.run(
        # Next I create a Scene object that allows me to string the layers together. In this case I only have 1 layer
#    scene.Scene(
            # And lastly I create the layer that we made above inside of the new scene
#        HelloWorld()
            
#     )
# )
if __name__=='__main__':
	logger = multiprocessing.log_to_stderr()
	logger.setLevel(multiprocessing.SUBDEBUG)
	video = cv2.VideoCapture(0)
	director.init()

	cocos()
	#t2 = threading.Thread(target=WatchInit, args=[])
	#t1.start()
	#t2.start()

	#p1 = multiprocessing.Process(target = director.run(scene.Scene(InputExample)), args=())
	#p1 = multiprocessing.Process(target = cocos())
	#p1.daemon = False
	#p2 = multiprocessing.Process(target = WatchInit())
	#p2.daemon = False
	#WatchInit()
	#print(h)

	#director.run(scene.Scene(InputExample()))

	#p2.start()
	#p1.start()
	#p1.join()
	#p2.join()

     
    
     
     
     
     # And once again the same init code
     #director.run(scene.Scene(InputExample()))
     #HelloWorld()
     #tmp = HelloWorld()

#if __name__=='__main__':
  #  for count in [10**4, 10**5, 10**6]:
       # queue = Queue()   # reader() reads from queue
                          # writer() writes to queue
       # reader_p = Process(target=reader, args=((queue),))
       # reader_p.daemon = True
       # reader_p.start()        # Launch reader() as a separate python process

       # _start = time.time()
       # writer(count, queue)    # Send a lot of stuff to reader()
       # reader_p.join()         # Wait for the reader to finish
       # video = cv2.VideoCapture(0)
       # director.init()
       # p1 = Process(target = director.run(scene.Scene(InputExample())))
       # p1.start()
       # print ("Sending %s numbers to Queue() took %s seconds" % (count, 
            #(time.time() - _start)))
