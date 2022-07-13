import numpy as np
import pandas as pd

class Die:
    """
    PURPOSE: This class creates a die of any number of sides, with default weights of 1. Methods that can be applied to the die include changing the weight (change_weight), rolling the die (roll_die), and showing the die (show_die).
    
    INPUT:
    arr   array of die faces
    
    OUTPUT: 
    depends on the method applied
    """
    __diedf = 0
    
    def __init__(self, arr):
        """
        PURPOSE: Initializes the new die object and saves faces and weights to a private dataframe that is shared by other methods of this class.
        
        INPUT:
        arr   array of die faces
        
        OUTPUT:
        none
        """
        self.n = arr.tolist()
        self.weights = np.ones(len(self.n))
        self.__diedf = pd.DataFrame({'side':self.n,\
                                   'weight':self.weights})
        self.__diedf = self.__diedf.set_index('side')
    
    def change_weight(self, face_val, new_weight):
        """
        PURPOSE: Change the weight of a single side of the die.
        
        INPUTS:
        face_val    the face value to be changed (str/float/int)
        new_weight  the desired weight of specified die (float/int)
        
        OUTPUT:
        none
        print statements if incorrect inputs are provided
        """
        if face_val in self.n:
            
            if type(new_weight) == float:
                self.__diedf.loc[face_val, 'weight'] = new_weight
            elif type(new_weight) == int:
                new_weight = float(new_weight)
                self.__diedf.loc[face_val, 'weight'] = new_weight
            else:
                print('The new weight is not the correct data type - please input a float or an integer')
                
        else:
            print('This face value is not valid because it is not found.')
    
    def roll_die(self, num_rolls = 1):
        """
        PURPOSE: Rolls the die one or more times
        
        INPUT:
        num_rolls   the number of times to roll the die - defaults to 1 (int)
        
        OUTPUT:
        results    a list of the outcomes of the die rolls
        """
        results = []
        
        for i in range(num_rolls):
            result = self.__diedf.reset_index()['side']\
            .sample(weights=self.__diedf.reset_index()['weight'])\
            .values[0]
            results.append(result)
            
        return results
    
    def show_die(self):
        """
        PURPOSE: Show the user the die's current set of faces/weights.
        
        INPUT:
        none
        
        OUTPUT:
        the dataframe of the die created in the initializer
        """
        return self.__diedf
    
    
class Game:
    """
    PURPOSE: This class plays the dice game by rolling one or more of the same kind of dice one or more times. Note that each die in a given game will have the same number of sides and associated faces, but each die may have its own weights. This class keeps the results of the most recent play.
    
    INPUT:
    die_lst    a list of die objects
    
    OUTPUT:
    depends on the method applied
    """
    
    def __init__(self, die_lst):
        """
        PURPOSE: Initializes a game.
        
        INPUT:
        die_lst    a list of die objects
        
        OUTPUT:
        none
        """
        self.die_lst = die_lst
        
    def play(self, num_rolls):
        """
        PURPOSE: Rolls the dice however many times are specified in num_rolls and saves the results of the game to a private dataframe. 
        
        INPUT:
        num_rolls    number of rolls for the group of dice (int)
        
        OUTPUT:
        none - saves the results to a private dataframe
        """
        results = []
        for die in self.die_lst:
            die_rolls = []
            for i in range(num_rolls):
                result = die.show_die()\
                .reset_index()['side']\
                .sample(weights=die.show_die()\
                        .reset_index()['weight'])\
                .values[0]
                
                die_rolls.append(result)
            results.append(die_rolls)
    
        self.__play_df = pd.DataFrame(results)
        self.__play_df.index.name = 'die_number'
        self.__play_df.T.index.name = 'roll_number'
    
    def show_results(self, df_form = 'wide'):
        """
        PURPOSE: Shows the user the results of the most recent play in the game by passing the dataframe to the user in a specified format.
        
        INPUT:
        df_form    optional argument that takes the form "wide" or "narrow" for the dataframe
        
        OUTPUT:
        either the narrow or wide form of the private dataframe containing play results
        """
        if df_form == 'narrow':
            narrow_df = pd.DataFrame(self.__play_df.stack()).rename(columns={0:'face_rolled'})
            return narrow_df
        elif df_form == 'wide':
            return self.__play_df.T
        else:
            raise Exception("Form must be set to either 'wide' or 'narrow'")
            

class Analyzer:
    """
    PURPOSE: This class takes the results of a single game and computes various descriptive statistical properties about it. 
    
    INPUT:
    game_results    a Game object with shown results (wide or narrow) as the input (dataframe)
    
    OUTPUT:
    depends on method applied
    """
    def __init__(self, game_results):
        """
        PURPOSE: Initializes the analyzer.
        
        INPUT:
        game_results   a Game object with shown results (wide or narrow) as the input (dataframe)
        
        OUTPUT:
        none
        """
        self.game_results = game_results
    
    def comp_jackpot(self):
        """
        PURPOSE: Computes how many times the game resulted in all faces of the dice being identical, or in other words, the "jackpot."
        
        INPUT:
        none
        
        OUTPUT:
        the number of times the game had a jackpot (int)
        """
        if len(self.game_results.columns) == 1:
            game_unstacked = self.game_results.unstack(level = 0)
            jackpots = 0
            self.jackpot_df = pd.DataFrame([])
    
            for i in range(len(game_unstacked)):
                arr = game_unstacked.loc[i, :]
                if np.all(arr == arr[0]) == True:
                    jackpots += 1
                    for j in range(len(game_unstacked.columns)):
                        self.jackpot_df.loc[i, j] = arr[0]
                else:
                    continue
            self.jackpot_df.index.name = 'roll_number'
            return jackpots
        else:
            jackpots = 0
            self.jackpot_df = pd.DataFrame([])
    
            for i in range(len(self.game_results)):
                arr = self.game_results.loc[i, :]
                if np.all(arr == arr[0]) == True:
                    jackpots += 1
                    for j in range(len(self.game_results.columns)):
                        self.jackpot_df.loc[i, j] = arr[0]
                else:
                    continue
            self.jackpot_df.index.name = 'roll_number'
            return jackpots
        
    def comp_combo(self):
        """
        PURPOSE: Computes the distinct combinations of faces rolled, along with their counts.
        
        INPUT:
        none
        
        OUTPUT:
        none - results are stored as combo_df (dataframe)
        """
        # narrow df
        if len(self.game_results.columns) == 1:
            self.combo_df = self.game_results.unstack(level = 0).apply(lambda x:\
                                                                       pd.Series(sorted(x)),\
                                                                       1).\
            value_counts().to_frame('n')

            
        else: # if the game is provided as a wide df
            self.combo_df = self.game_results.apply(lambda x:\
                                                    pd.Series(sorted(x)),\
                                                    1).value_counts().to_frame('n')
            
    def count_faces_per_roll(self):
        """
        PURPOSE: Compute how many times a given face is rolled in each event/roll.
        
        INPUT:
        none
        
        OUTPUT:
        none - results are stored as val_counts_df (dataframe)
        """
        # narrow df
        if len(self.game_results.columns) == 1:
            game_unstacked = self.game_results.unstack(level = 0)
            
            self.val_counts_df = game_unstacked.apply(pd.Series.value_counts,\
                                                      axis = 1).fillna(0)
                
        # wide df
        else:
            self.val_counts_df = self.game_results.apply(pd.Series.value_counts,\
                                                         axis = 1).fillna(0)
        


