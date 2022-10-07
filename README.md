# Rock-paper-scissors
An ai to play rock paper scissors

About the game:

Rock paper scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors"

Requirements:

Python 3
Keras
Tensorflow
OpenCV

Set up instructions:

Clone the repo.
$ git clone https://github.com/tech-axis/rock-paper-scissors.git
$ cd rock-paper-scissors
Install the dependencies
$ pip install -r requirements.txt
Gather Images for each gesture (rock, paper and scissors and None): In this example, we gather 200 images for the "rock" gesture
$ python3 gather_images.py rock 200
Train the model
$ python3 train.py
Test the model on some images
$ python3 test.py <path_to_test_image>
Play the game with your computer!
$ python3 play.py
