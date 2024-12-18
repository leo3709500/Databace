import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
class Img_setting:
    def __init__(self):
        self.background = os.path.join(script_dir, 'background.png').replace(os.sep, '/')
        self.background_2 = os.path.join(script_dir, 'background_2.png').replace(os.sep, '/') 
        self.icon1 = os.path.join(script_dir, '1.png').replace(os.sep, '/') 
        self.icon2 = os.path.join(script_dir, '2.png').replace(os.sep, '/') 
        self.icon3 = os.path.join(script_dir, '3.png').replace(os.sep, '/') 
        self.icon4 = os.path.join(script_dir, '4.png').replace(os.sep, '/')