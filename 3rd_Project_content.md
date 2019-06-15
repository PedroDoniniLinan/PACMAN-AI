# *Subject* : Bayes' Nets

**Problem** :Pacman has entered a world of mystery. Initially, the entire map is invisible. As he explores it, he learns information about 
neighboring cells. The map contains two houses: a ghost house, which is probably mostly red, and a food house, which is probably mostly 
blue. Pacman's goal is to enter the food house while avoiding the ghost house. Pacman will reason about which house is which based on his observations, and reason about the tradeoff between taking a chance or 
gathering more evidence. To enable this, you'll implement probabilistic inference using Bayes nets.

All algorithms to operate with the Bayes' Nets and the agent itself can be found in the "bayesAgents.py", "factorOperation.py", 
"inference.py" files.

1. Bayes Net structure: the constructBayesNet function in bayesAgents.py. constructs an empty Bayes net.

2.  Bayes Net Probabilities: the fillXCPT, fillYCPT, fillHouseCPT and fillObsCPT functions in bayesAgents.py. take the Bayes net 
constructed, and specify the factors governing the X and Y position, the houses and observation variables. 

3. Join Factors: the joinFactors function in factorOperations.py takes in a list of Factors and returns a new Factor whose 
probability entries are the product of the corresponding rows of the input Factors.

4. Eliminate: the eliminate function in factorOperations.py takes a Factor and a variable to eliminate and returns a new Factor 
that does not contain that variable. This corresponds to summing all of the entries in the Factor which only differ in the value 
of the variable being eliminated.

5. Normalize: the normalize function in factorOperations.py takes a Factor as input and normalizes it, that is, it scales all of the 
entries in the Factor such that the sum of the entries in the Factor is 1.

6. Variable Elimination: the inferenceByVariableElimination function in inference.py. It answers a probabilistic query, which is 
represented using a BayesNet, a list of query variables, and the evidence.

7. Marginal Inference: the inferenceByVariableElimination function is used to compute the marginal distribution over positions of the 
food house, then return the most likely position. This information is used by Bayesian Pacman, who wanders around randomly collecting 
information for a fixed number of timesteps, then heads directly to the house most likely to contain food.
