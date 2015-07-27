from browser import window, document
from random import randint
from javascript import JSObject, JSConstructor

w = window.open("", "")


# depends on pixi.js 
PIXI = JSObject(window.PIXI)
PIXI_loader = JSObject(PIXI.loader)
PIXI_loader.reset()

PIXI_Sprite = JSConstructor(PIXI.Sprite)
PIXI_Texture = JSConstructor(PIXI.Texture)
PIXI_Rectangle = JSConstructor(PIXI.Rectangle)


class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.PIXI = PIXI_Rectangle(x,y,w,h)
    
    @property
    def center(self):
        return (self.x + self.w//2, self.y + self.h//2)
    
    @center.setter
    def center(self, value):
        c = self.center
        self.x += value[0] - c[0]
        self.y += value[1] - c[1]
        
class ImageAsset(object):
    def __init__(self, url):
        self.url = url
        self.texture = PIXI.Texture.fromImage(url, False)

class Sprite(object):
    def __init__(self, texture, frame):
        

if __name__ == '__main__':
    def animate(fake):
      w.requestAnimationFrame(animate)
      RENDERER.render(STAGE)
    
    bunnyurl = "bunny.png"
    print("ggame test.")
    bunny = ImageAsset(bunnyurl)
    Stage = JSConstructor(PIXI.Container)
    STAGE = Stage()
    RENDERER = PIXI.autoDetectRenderer(1000,650, {'transparent':True})
    frame = PIXI_Rectangle(0,0,30,30)

    s1 = PIXI_Sprite(PIXI_Texture(bunny.texture, frame))
    STAGE.addChild(s1)
    w.document.body.appendChild(RENDERER.view)
    w.requestAnimationFrame(animate)

