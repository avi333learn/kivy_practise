# BOUNCING BALL GUI
---
### Concept:
When we press "GO" button, green ball starts moving. When ball touches edges of wall, it bounces in such way that it always remain visible on screen. <br/>
### Requirements:
1. python 3.6 to 3.9
2. kivy 2.0.0 <br/><br/>
### Output:
![bounce_kivy_app](https://user-images.githubusercontent.com/70983924/139490394-6c5bf01a-da65-4167-9dcb-72135782be9d.png)

### Working:
1. When button "GO" is pressed, function `self.repeater()` is called which repetatively calls `self.anim1()` after every 0.05 seconds.<br/>
2. `self.anim1()` gives old position to `self.direction()` which returns x and y values where circle should be next. These new values are implemented by assigning them to `self.el.pos` which is basically an argument of ellipse.<br/>
3. `self.direction()` decides future point. There 2 thing used to calculate direction:<br/>
   * Magnitude: this is decided by list `inc_pt` where `inc_pt[0]` is value for x and `inc_pt[1]` is value for y.
   * Direction: this is either +1 or -1 and is stored in list `vector1` where `vector1[0]` is value for x and `vector1[1]` is value for y.<br/>

There is default magnitide (2, 2) and default direction (1, 1). "if statement" becomes true when ball touches any wall and then value in vector1 is changed such that ball remains within visible area.
