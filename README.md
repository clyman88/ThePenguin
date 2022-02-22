# ThePenguin

#### Link to Google Doc: [Here](https://docs.google.com/document/d/1Sf24Mtsomg_Ii05QBMTFbYv3pOCejpcIwBJ-gdY9PqM/edit?usp=sharing)

#### Link to Schedule: [Here](https://docs.google.com/spreadsheets/d/1rT3I_5nSTPqYd5fbr5m2Sy22h2AO5hXBsvJUreVN8uk/edit?usp=sharing)


## The Problem & Solution

The goal of this project is to map the flight path of a payload dropped by a kite. How would this be helpful or practical? Consider a skydiver jumping out of a plane, or a rocket part returning back to earth from orbit. Wind patterns make it really difficult to predict where exactly a payload will land when it travels down to the ground. But it’s useful to be able to estimate this, since it allows for the payload to be collected and for its flight path to be recorded. This project aims to do this by using a gyroscope to map the 3D path of a payload dropped from a kite that’ll reach the ground using a parachute.


## Scope

The project will consist of three main parts:
A delta kite (the lift), an outside box (the payload container), inner box (the data-recording payload)

In addition to this, there’ll be a pivacek carabiner to tie the outer box to the kite, suspending it with a network of strings, a release mechanism for the payload to drop (this will involve a servo), and a parachute.

The coding challenge will be in learning how to use the gyroscope, and for the CAD it’ll be designing the boxes (likely using wood) as well as designing the servo mechanism. 

If the scope of the project is too big, we’ll scale down to only using the outside box and not using a payload; only the 3D flight of the kite would be mapped.


## Risk Mitigation

The main risk will be in dropping the payload so that it isn’t damaged and in making sure the parachute works so that the payload lands down smoothly. Here are the different release mechanisms we’re considering:

![Release_Mechanism_Ideas](https://github.com/clyman88/ThePenguin/blob/main/media/IMG_7485.JPG)


## How Code Will Work

The code for this project will involve learning how to use a gyroscope (basically, a souped-up accelerometer that is able to record an object's path through space) and coding the servo(s) to release the payload. At a certain elevation or time limit, the servo will activate, dropping the payload. If there’s spare time, to take this a step further, the servo could be activated with a remote signal.


## Design

Here is how the project will look:

![Penguin Diagrams](https://github.com/clyman88/ThePenguin/blob/main/media/IMG_7484.jpg)

This is how the picavet carabiner will attach the outer box:

![Picavet_Mechanism](/media/Picavet.gif)

## Resources / Bill of Materials:

* Kite materials: [delta kite, kite line, & a handle](https://www.amazon.com/Breeze-Rainbow-Conyne-Delta-6-Feet/dp/B00C9T4HDG/ref=sr_1_2?crid=XFQJCKMACLOF&keywords=7%2Bfoot%2Bdelta%2Bkite&qid=1644852021&sprefix=7%2Bfoot%2Bdelta%2Bkite%2Caps%2C76&sr=8-2&th=1) 
* Wood planks from the Sigma Lab (anchored using glue, T-slots, or tape. Both the outer- and inner-box will be made of wood.
* 3 medium sized washers and string/line to link them
* 2 picavet carabringers
* Hardware: Raspberry Pi, gyroscope, servo, and battery
* 4 eye screws 
* Fabric for the parachute
* Some gloves to prevent rug burn from the kite


## Credit/Inspiration:

This project provided us inspiration:
[Project1](https://wTww.instructables.com/Kite-Aerial-Photography-Picavet-System-Fun-Simple-/)
[Project2]http://richardhayler.blogspot.com/2015/09/skycademy-hab-payload-testing-with-kite.html

Finally, thanks to Mr. Dierolf for the idea and also Mr. Miller for advice.
