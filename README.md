# montecarlo
This includes the final project for DS5100

### Metadata
Name: Eve Schoenrock
UserID: ufu2rg
Project Name: Monte Carlo Simulator

### Synopsis
First install and import the code.

Installation is possible once the user is in the repo. Run the following command:
```
pip install -e .
```
This command will install all packages specified in the setup.py file of the repo.

To import the module in the montecarlo package, run this code in your file.
```
from montecarlo.montecarlo import Die
from montecarlo.montecarlo import Game
from montecarlo.montecarlo import Analyzer
```


The first step is to create dice. Create dice by specifying faces in an numpy array and passing it to Die.
```
die = Die(np.array([1, 2, 3]))
die2 = Die(np.array(['a', 'b', 'c'])
```
As you can see, die can have faces as either letters or numbers, but data types cannot be mixed for a given die. 
```
die2.change_weight('a', 4)
```
```
die2.roll_die(5)
```
```
die2.show_die()
```
Within the Die class, you can take advantage of the `change_weight`, `roll_die`, and `show_die methods`. For more information on these methods, see their docstrings in the API description.

Next, you will want to play a game. Start by instantiating a Game object, passing it a list of dice (Die objects) with similar faces. Here, we make a list of 3 dice.
```
die_lst = [die, die, die]
game = Game(die_lst)
game.play(10)
results = game.show_results()
```
Now that a game exists, you can `play` it and `show_results`. Be sure to save the output of `show_results` to store the game dataframe that is created once the game has been played. For more information on these methods, see their docstrings in the API description.

Lastly, you will have the ability to analyze games. Do this by creating an Analyze object, which takes the `show_results` method of the Game class as input.
```
analyzer = Analyze(results)
```
From here, you can implement methods to count the number of jackpots in a given game (`comp_jackpot`), create a new dataframe with the count of each specific combination of faces (`comp_combo`), and show the number of times a given face appears in each roll of a game (`count_faces_per_roll`).
```
analyzer.comp_jackpot()
```
```
analyzer.comp_combo()
```
```
analyzer.count_faces_per_roll(1)
```
You will find a detailed description of each of these methods in the API description section.

### API description
The classes and their public methods and attributes are detailed in the following lines. The classes available are Die, Game, and Analyzer.

1. First there is the Die class which consists of the following public methods: `[change_weight(face_val, new_weight), roll_die(num_rolls = 1), show_die()]`. See below for their docstrings.

```
help(Die.change_weight)
```
    The docstring for `change_weight`:
    Help on function change_weight in module montecarlo.montecarlo:

    change_weight(self, face_val, new_weight)
        PURPOSE: Change the weight of a single side of the die.
        INPUTS:
        face_val    the face value to be changed (str/float/int)
        new_weight  the desired weight of specified die (float/int)
        OUTPUT:
        none
        print statements if incorrect inputs are provided
    
```
help(Die.roll_die)
```

    The docstring for `roll_die`:
    Help on function roll_die in module montecarlo.montecarlo:

    roll_die(self, num_rolls=1)
        PURPOSE: Rolls the die one or more times
        INPUT:
        num_rolls   the number of times to roll the die - defaults to 1 (int)
        OUTPUT:
        results    a list of the outcomes of the die rolls
    
* `roll_die` takes an `int` as optional input for the number of rolls and returns the results of however many rolls were specified by the user.

```
help(Die.show_die)
```

    The docstring for `show_die`:
    Help on function show_die in module montecarlo.montecarlo:

    show_die(self)
        PURPOSE: Show the user the die's current set of faces/weights.
        INPUT:
        none
        OUTPUT:
        the dataframe of the die created in the initializer
    
* `show_die` returns a dataframe that shows the number of sides the die has and the values of its faces.

2. Second is the Game class which consists of the following public methods: `play(num_rolls)` and `show_results(df_form)`. See below for their docstrings.

```
help(Game.play)
```

    The docstring for `play`:
    Help on function play in module montecarlo.montecarlo:

    play(self, num_rolls)
        PURPOSE: Rolls the dice however many times are specified in num_rolls and saves the results of the game to a private dataframe. 
        INPUT:
        num_rolls    number of rolls for the group of dice (int)
        OUTPUT:
        none - saves the results to a private dataframe

```
help(Game.show_results)
```

    The docstring for `show_results`:
    Help on function show_results in module montecarlo.montecarlo:

    show_results(self, df_form='wide')
        PURPOSE: Shows the user the results of the most recent play in the game by passing the dataframe to the user in a specified format.
        INPUT:
        df_form    optional argument that takes the form "wide" or "narrow" for the dataframe
        OUTPUT:
        either the narrow or wide form of the private dataframe containing play results

* `show_results` takes the optional input of 'narrow' or 'wide' for how the user would like to see the dataframe returned (the default value is 'wide') and returns a dataframe of either narrow or wide format.

3. Last is the Analyzer class which has the following public methods: `[comp_jackpot(), comp_combo(), count_faces_per_roll(count_val)]`. See below for their docstrings. Note that all methods in the Analyzer class make use of the public attribute, `game_results`, which is the dataframe that was passed to the Analyzer object.

```
help(Analyzer.comp_jackpot)
```

    The docstring for `comp_jackpot`:
    Help on function comp_jackpot in module montecarlo.montecarlo:

    comp_jackpot(self)
        PURPOSE: Computes how many times the game resulted in all faces of the dice being identical, or in other words, the "jackpot."
        INPUT:
        none
        OUTPUT:
        the number of times the game had a jackpot (int)

* `comp_jackpot` returns the number of jackpots that were found in a given game (the number of times all dice fell on the same face for a given roll). Additionally, the public attribute, `jackpot_df` is housed under this method which shows the dataframe of jackpots that occurred in the game with the roll number of the jackpot as its index.

```
help(Analyzer.comp_combo)
```

    The docstring for `comp_combo`:
    Help on function comp_combo in module montecarlo.montecarlo:

    comp_combo(self)
        PURPOSE: Computes the distinct combinations of faces rolled, along with their counts.
        INPUT:
        none
        OUTPUT:
        none - results are stored as combo_df (dataframe)
        
* `comp_combo` does not return anything, but it creates the public attribute, `combo_df` which shows the dataframe of combinations that occurred in the game and the number of times each combination appeared. `combo_df` is a MultiIndex dataframe where the combination constitutes the index.

```
help(Analyzer.count_faces_per_roll)
```

    The docstring for `count_faces_per_roll`:
    Help on function count_faces_per_roll in module montecarlo.montecarlo:

    count_faces_per_roll(self, count_val)
        PURPOSE: Compute how many times a given face is rolled in each event/roll.
        INPUT:
        count_val    the face value to look for (int/float/str - must be an existing face value)
        OUTPUT:
        none - results are stored as val_counts_df (dataframe)
        
* `count_faces_per_roll` does not return anything, but it creates the public attribute, `val_counts_df` which shows the dataframe of rolls and the number of times a given value appeared in each roll. The roll number is the index of this public attribute.

### Manifest
Files in the repo include:
* montecarlo
    * montecarlo.py
    * montecarlo_tests.py
    * __init__.py
* README.md
* setup.py
* .gitignore
* LICENSE
* scenarios.ipynb
* montecarlo_results.txt
