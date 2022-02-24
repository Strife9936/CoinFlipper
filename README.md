# CoinFlipper
Coin Flipping Simulation(How many times could a coin land on its edge?)

Project Documentation
	Background: The overall context of this project is to simulate the flipping of a coin, but more specifically an American nickel. 
  What I wanted to achieve with this project is to see how many times a nickel could land on its side in 6000 attempts. 
  
  Hypothesis: As for the hypothesis that I created, I believed that a nickel could not land on its side not even once throughout all 6000 flips. 
  
  Data: Based on a research paper from October 1993, there was a computational model constructed to simulate specifically an American nickel flipping 6000 times and landing approximately 1 out of the 6000 attempts or in other words a 0.02% chance of landing on its side. 
  In this research paper, they took into account the motion of the coin while being flipped, the collision of the coin with the ground, and phase of transition 
  before the coin reaches a state of equilibrium. One of the possible biases with this data is the fact that the model used in assumption was described as a “perfect, 
  incompressible cylinder” when this may not be the case for every American nickel out there. There could be damaged nickels, nickels with differing ridges, nickels with different
  minting designs that could slightly alter its weight. We could also consider other potential problems such as the type of material the coin is landing on such as carpet, wood, rubber, etc. 
  There’s also the possibility of considering how people prefer to flip a coin such as flicking upwards with their thumb, doing an underhand toss, etc. 
  Finally, there are also other external factors to consider such as an individual’s environment, whether or not they are performing this experiment indoors or outdoors, and the weather conditions if they are to perform this outdoors
  
  Analysis: When it came down to importing the data, I had to figure a few things. First, I had to analyze and see what the actual odds of landing on heads, tails, and the Edge
  of the coin were out of 6000 attempts. We already know that landing on the Edge of a coin is a 1/6000 probability, but for heads and tails we could assume it’s a 50/50 chance. 
  So for all sides to get respective probability weight, we would have to subtract 6000 by the probability of the coins edge which is 1. This gives us 5,999 and if we divide that
  by 2, then that would leave us with a 50/50 probability on both sides with 2999.5. We would then have to loop/repeat this sequence for a number of 6000 times. 
  Now this could be done in two ways; with a for loop or by utilizing the return choice method which uses an integer K which defines the length of the returned list. 
  It’s also worth noting that utilizing the random.choice method returned more accurate results compared to using the import random module. The import random module is more 
  accurate when measuring the probability of an even set of items. Random.choice allows us to gain a more accurate answer since it requests for the weighted possibility of each 
  value.

  Conclusion: Through several attempts, we could notice the coin landing on its edge for a number of 0,1,or even 2 times per simulation. 
  There were very few instances in the simulation where the coin would actually land 4 times or more on its edge. Although the results come very close, it doesn’t quite mirror
  an exact 1/6000 chance. If we incorporated more physics and higher level mathematics, then this could definitely mirror the same results as mentioned from the research paper.
