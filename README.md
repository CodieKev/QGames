# QGames

## Quantum Board Run

Game consist of 2 player system trying to eliminate each other.  
In each term first the defending player is allwod to move on the board and after that the attacking player is allowed to place a bomb on the defenders board.  
After this the board updates with the new position of defending player and if the bomb damages him his health is redused by one heart. Once the defender is out of heart the attacking player wins.
After each term the attacking and defending switches.
### Rules:
+ Player defending is allowed to move in 2 different ways:
  - Classical : Here player can move to any of the 8 positions surrounding him (like a king in chess), and the position of the coin will show the predicted position of the player.
  - Quantum : Here player is allowed to make a superposition of his position (denoted by the coin) keeping in mind that the current position should be in the superposition. And       the player position will be updated according to the collaps of his superposition state.
+ Attacking Player can place the bomb only at one of the blocks on opponents board and as there is no superposition only "X" gate is permited to use.
+ The Bomb explodes in a way that it damages on the board with a "+" sign and if player is in those position he will receive the dammage. 
+ After the selection of the state in any of the defending and attacking cases one should press enter to fix the state and then press and after that presses enter to state the count down for the second players turn.
+ While making the state remember that controled gate costs much more than the single qubit gates so to compensate for that if you choose to apply controled gates the whole collumn will be unusable for any other gates.
+ Permited Gates are :
  - H
  - X
  - CH
  - CX
  - CCX
  - MCX (multiple controle x gate)
+ Circuit Arrangement:   
  ![](Quantum_Board_Run/Resource/Circuit_resized.jpg )  
+ Board Arrangement:  
  ![](Quantum_Board_Run/Resource/Board_resized.jpg ) 

## Authors

* **Rohit Prasad** - [CodieKev](https://github.com/CodieKev) - [Rohit Prasad](https://www.linkedin.com/in/rohit-prasad-codie-5845b11a9/)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
