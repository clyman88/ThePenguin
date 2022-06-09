# ThePenguin - Final Submission

## This README contains a summary and reflection of our Pi in the Ski Project: The Penguin

#### Link to Google Doc: [Here](https://docs.google.com/document/d/1Sf24Mtsomg_Ii05QBMTFbYv3pOCejpcIwBJ-gdY9PqM/edit?usp=sharing)
This doc was used in the inital planning/brainstorm of the project.

#### Link to Schedule: [Here](https://docs.google.com/spreadsheets/d/1rT3I_5nSTPqYd5fbr5m2Sy22h2AO5hXBsvJUreVN8uk/edit?usp=sharing)
This was the schedule we created at the beginning of the year. While we ended up straying off from our initial deadlines, we compared our initial plan to what actually happened and were able to reflect on what we could have done better as a result. 


## Overview of the Project & Design Decisions

Should include a history of our drawings/sketches.
How the arm lengths had to be changed. 
How the holes were to two small for the usb chargers to fit into. 
Switching from two servos to one servo -- being more efficient


## Constructing the Box / Materials Used

### The initial materials used that we planned was as follows:
- Kite materials: delta kite, kite line, & a handle
- Wood planks from the Sigma Lab (anchored using glue, T-slots, or tape. Both the outer- and inner-box will be made of wood.
- 3 medium sized washers and string/line to link them
- 2 picavet carabringers
- Hardware: Raspberry Pi, gyroscope, servo, and battery
- 4 eye screws
- Fabric for the parachute
- Some gloves to prevent rug burn from the kite

### These were the materials incorporated into the final version:
- The kite, string, and handle. We stuck with a delta kite and bought a kite set from Amazon. 
- Acryllic from the sigma lab. Acryllic was lighter and more vertasile than wood, as it was easier to laser cut and put together. Acryllic was used for both the inner box and outer box.
- Hardware: Raspberry Pi, gryoscope (mpu 6050), two micro servos, a rechargeable battery pack, power boost 500c, and a button, and a power switch. The powerboost, button, and power switch were all added so that the project could work without being plugged into a computer, which was neccesary for it to fly. Having a rechargeable battery and switch also made the project set up much easier, though we did not know that a red light on the power switch meant low battery (we learned the hard way in the 1st launch)
- Instead of eye screws, which would have protruded for the outer box and have been laced with string, we used an easier solution: simply cutting holes in the outer box in a cross formation and then tying the 2 picavet carabringers using them. 
- Finally, we borrowed our parachute initially from Max Sweet and then finally from Alden Dent and William Keenan due to lack of time. The parachute was held in place by threading the four strings through holes in the inner box and then tying a knot to lock them in place.

## The circuit diagram and final code:

### Circuit Diagram
![Circuit Diagram](./media/circuit_diagram)

### Commented code
[Final code](./code/project_code.py)
Here is the link to the csv file we recorded during our flight: [Final csv](./code/data.csv)


## OnShape Work / CAD Renderings

Insert pictures of the OnShape views of the project


## Problems Overcame / Lessons Learned

* The primary lesson that we took away from this project is that it tends to be better to not leave final tweaks and design changes to the last few days. We should have worked faster and stuck more diligently to the schedule we had created. If we had, we would have been more structured and driven, knowing what we had to work on each day. Because we did stray off our schedule, we got behind and had to make some last minute changes (i.e. fixing servo jitter before launch, charging/changing batteries the day of launch, allowing the code permission to create a .csv file as a daemon (thanks to Alden Dent for helping fix this). 

* At first, the kite wasn't going high enough to stay in the air. We fixed this problem by testing several different lengths of the payload from the kite and recording the best one. This helped us establish a standard for where we would put the payload. 

* For the code, it was initially tricky to print both the acceleration and gyro data from the mpu onto the same line of a csv row each iteration. This was because the mpu data was formatted as tuples of strings. To solve this, we had to Google the differences between lists and tuples and what a '%.2f' meant (inserting a variable with two decimals), and look into the library of the mpu. The IDE PyCharm was very helpful in solving this, as it made it easy to access the mpu library and see how the data was formatted.

* Pi  upload and recharging holes -- we designed holes that were supposed to be large enough to fit the metal part of a USB cord, but it turns out that the holes had to larger still to fit the rubber encasing of a USB cord. We did not have time to change our design for this, so we had to take off the walls each time. 

* The design initially used two servos to retract the inner box while also suspending it. However, Mr. Miller and Mr. H offered us their engineering wisdom in explaining that we only had to use one servo to turn two racks. This was indeed a much more practical method, so we redesigned the box with one servo in the middle.

* The initial servo racks did not fit their correponding rails, meaning the servo could not retract. We fixed this by sandpapering the rails to be larger and then later on recuting the servo racks to be the correct size. We also laser cut several racks so that we would have spares in case on broke. 


## Credit/Inspiration:

This project provided us inspiration:
[Project1](https://wTww.instructables.com/Kite-Aerial-Photography-Picavet-System-Fun-Simple-/)
[Project2]http://richardhayler.blogspot.com/2015/09/skycademy-hab-payload-testing-with-kite.html

Finally, thanks to Mr. Dierolf for the idea and also Mr. Miller for advice.
