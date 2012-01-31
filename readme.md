This is an entry for the Kivy game design competition (Jan 31st 2011)

By no means is this piece of software a finished piece. I was pretty crunched for time when I decided to enter the game design competition, so I couldn't honour many Python idioms when coding this up. Forget Python idioms, to get stuff working at times I chose to overrule many basic OOP concepts as I had recently learnt them up and didn't have the luxury of implementing them out due to lack of time. 

At people who have been directed to this project to learn about Kivy,the framework, I suggest you wait for a couple of weeks by when I shall refactor this code to make it easy to understand and maintain. Kivy is quite beautifully designed and I wouldn't want you to be scared by this code :P

### Some specific details about the code:

* The entire app was squarely aimed at Tablets with **multitouch** played in a **landscape** format. It plays just fine on a PC, but you will miss the horizontally aligned 'winner screens' that I have designed for best use on a tablet.

* The screen resolution I have used throughout this project is 1280 X 736. (736 is used instead of 800 to give way for the menubar in most Operating Systems).I tried very hard to implement it using the 'auto' resolution mode in Kivy Config, but it simply wouldn't work. So I had to hardcode the most common tablet res into the app.

* I have used kivy.core.audio for playing a catchy track during the game. While this runs smoothly on my Ubuntu machine, the App force closed on an android tablet. So if you are trying this on Android, do comment out the sections by searching for "audio android" in main.py

* I had a nice time figuring out how to detect collisions in what appears to be a simple game at first sight. I went from an 
    * O(n^2) implementation ( I was checking each point on snake1 with each point on snake2)
    * to an O(n) implementation which was horribly innacurate(It used to check for occupied areas around a bounding box near each snake's head)
    * To finally maintain a central boolean array of occupied places. This is so simple and efficient and remains so, even when I add more snakes into the game.I should probably admit that Stack Overflow nudged me in this direction. Also python must have a O(log n) complexity look up a particular index of a 1D array. So,my algo has the same complexity. :)
    
* I wish I made more use of the .kv file and the instant updation that it offers.

### The road ahead:

##### More game features:

* Smooth turns instead of right angled turns. 
    : This can be implemented this instant with a suitable value in Vector.rotate method, but I found that the gameplay suffered due to some some restrictions in the button press events.I need to read more into Button state and how to account for it from the Kivy Docs)
* Add options in the main menu to increase or decrease the difficulty. 
    : This is accomplished by faster and slower velocities of the snakes respectively)
* Add more spice to the game canvas by introducing speed-up collectibles, snake length-reducers and other usual arcade game items :)
* Support 4 players
    : This can also be implemented in just a couple of hours as the collision detection mechanism remains the same.


    
    
    
    
