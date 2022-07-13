import pandas as pd
import numpy as np
import unittest
from montecarlo.montecarlo import Die

class DieTestSuite(unittest.TestCase):
    """
    PURPOSE: This class will test the Die class using unittest.
    
    INPUT:
    none
    
    OUTPUT:
    none
    """
    def test_1_change_weight(self):
        """
        PURPOSE: Test whether or not the 'change_weight' method of the Die class functions properly. In particular, it checks that the weight of the 'a' face changes to 2 when specified.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array(['a', 'b', 'c']))
        die1.change_weight('a', 2)
        
        actual = die1.show_die().loc['a', 'weight']
        expected = 2.0
        self.assertEqual(actual, expected)
    
    def test_2_roll_die_default(self):
        """
        PURPOSE: Test whether or not the 'roll_die' method of the Die class functions properly. It tests the default value for the number of rolls, 1, making sure that the die rolled once.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        
        actual = len(die2.roll_die())
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_3_roll_die(self):
        """
        PURPOSE: Test whether or not the 'roll_die' method of the Die class functions properly. It tests when the roll number is 10, making sure that the die in the function is actually rolled 10 times.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die3 = Die(np.array([1, 2, 3, 4, 5, 6]))
        
        actual = len(die3.roll_die(10))
        expected = 10
        self.assertEqual(actual, expected)
    
    def test_4_show_die(self):
        """
        PURPOSE: Tests the 'show_die' method of the Die class. It develops a dataframe to compare against a dataframe formed by the 'show_die' method and makes sure they are the same.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die4 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die4.change_weight(3, 5)
        
        actual_df = die4.show_die().reset_index()
        expected_df = pd.DataFrame({'side': [1, 2, 3, 4, 5, 6],\
                                    'weight': [1, 1, 5, 1, 1, 1]})
        
        actual_lst = []
        for i in range(len(actual_df)):
            if actual_df.iloc[i, 1] == expected_df.iloc[i, 1]:
                actual_lst.append(1)
            else:
                actual_lst.append(2)
        
        actual = all(x == 1 for x in actual_lst)
        expected = True
        self.assertEqual(actual, expected)
        
        
from montecarlo.montecarlo import Game

class GameTestSuite(unittest.TestCase):
    """
    PURPOSE: This class will test the Game class using unittest.
    
        INPUT:
        none
        
        OUTPUT:
        none
    """
    def test_1_play(self):
        """
        PURPOSE: Tests the 'play' method of the Game class by checking that a set dataframe with length 5 and a dataframe made of a game played 5 times have the same length. 
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array([4, 5, 6]))
        die2 = Die(np.array([4, 5, 6]))
        die3 = Die(np.array([4, 5, 6]))
        dice = [die1, die2, die3]
        game1 = Game(dice)
            
        game1.play(5)
        game1_df = game1.show_results()
            
        actual_len = len(game1_df)
        expected_len = 5
        actual_width = len(game1_df.columns)
        expected_width = 3
            
        actual = actual_len == expected_len and actual_width == expected_width
        expected = True
        self.assertEqual(actual, expected)
            
    def test_2_show_results_narrow(self):
        """
        PURPOSE: Tests the 'show_results' method of the Game class (a narrow dataframe). It compares an integer for what the length of the resulting dataframe should be with the actual length of the dataframe.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array(['a', 'b', 'c']))
        die2 = Die(np.array(['a', 'b', 'c']))
        die3 = Die(np.array(['a', 'b', 'c']))
        dice = [die1, die2, die3]
        game1 = Game(dice)
            
        game1.play(5)
        game1_df = game1.show_results('narrow')
            
        actual_len = len(game1_df)
        expected_len = 15
        actual_width = len(game1_df.columns)
        expected_width = 1
            
        actual = actual_len == expected_len and actual_width == expected_width
        expected = True
        self.assertEqual(actual, expected)
        
    def test_3_show_results_wide(self):
        """
        PURPOSE: Tests the 'show_results' method of the Game class (wide dataframe). It compares the expected length and width of the resulting dataframe with the actual length and width of the dataframe to ensure they are the same.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array(['a', 'b', 'c']))
        die2 = Die(np.array(['a', 'b', 'c']))
        die3 = Die(np.array(['a', 'b', 'c']))
        dice = [die1, die2, die3]
        game1 = Game(dice)
            
        game1.play(50)
        game1_df = game1.show_results()
            
        actual_len = len(game1_df)
        expected_len = 50
        actual_width = len(game1_df.columns)
        expected_width = 3
            
        actual = actual_len == expected_len and actual_width == expected_width
        expected = True
        self.assertEqual(actual, expected)
        
        
from montecarlo.montecarlo import Analyzer

class AnalyzerTestSuite(unittest.TestCase):
    """
    PURPOSE: This class will test the Analyzer class using unittest.
    
        INPUT:
        none
        
        OUTPUT:
        none
    """
    def test_1_comp_jackpot_wide(self):
        """
        PURPOSE: Tests the 'comp_jackpot' method of the Analyzer class on a wide dataframe by checking that the output is an integer, which is expected.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array([1, 2, 3, 4, 5]))
        die2 = Die(np.array([1, 2, 3, 4, 5]))
        die3 = Die(np.array([1, 2, 3, 4, 5]))
        die2.change_weight(1, 3)
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(3)
        game_results_wide = game.show_results('wide')
            
        analyze_wide = Analyzer(game_results_wide)
        num_jackpots = analyze_wide.comp_jackpot()
            
        actual = type(num_jackpots)
        expected = int
        self.assertEqual(actual, expected)
            
    def test_2_comp_jackpot_nar(self):
        """
        PURPOSE: Tests the 'comp_jackpot' method of the Analyzer class on a narrow dataframe by checking that the actual output is an integer, which is expected.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array([1, 2, 3, 4, 5]))
        die2 = Die(np.array([1, 2, 3, 4, 5]))
        die3 = Die(np.array([1, 2, 3, 4, 5]))
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(3)
        game_results_nar = game.show_results('narrow')
            
        analyze_nar = Analyzer(game_results_nar)
        num_jackpots = analyze_nar.comp_jackpot()
            
        actual = type(num_jackpots)
        expected = int
        self.assertEqual(actual, expected)
        
    def test_3_comp_combo_wide(self):
        """
        PURPOSE: Tests the 'comp_combo' method of the Analyzer class on a wide dataframe by checking that the length of the resulting dataframe is an integer, which is expected, and signifies that a dataframe has been constructed.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array([1, 2, 3, 4, 5]))
        die2 = Die(np.array([1, 2, 3, 4, 5]))
        die3 = Die(np.array([1, 2, 3, 4, 5]))
        die2.change_weight(1, 3)
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(3)
        game_results_wide = game.show_results('wide')
            
        analyze_wide = Analyzer(game_results_wide)
        analyze_wide.comp_combo()
        num_combos = len(analyze_wide.combo_df)
            
        actual = type(num_combos)
        expected = int
        self.assertEqual(actual, expected)
        
    def test_4_comp_combo_nar(self):
        """
        PURPOSE: Tests the 'comp_combo' method of the Analyzer class on a narrow dataframe by checking that the length of the resulting dataframe is an integer, which is expected, and shows that a dataframe is created.
        
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array([1, 2, 3, 4, 5]))
        die2 = Die(np.array([1, 2, 3, 4, 5]))
        die3 = Die(np.array([1, 2, 3, 4, 5]))
        die2.change_weight(1, 3)
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(3)
        game_results_nar = game.show_results('narrow')
            
        analyze_nar = Analyzer(game_results_nar)
        analyze_nar.comp_combo()
        num_combos = len(analyze_nar.combo_df)
            
        actual = type(num_combos)
        expected = int
        self.assertEqual(actual, expected)
            
    def test_5_count_faces_per_roll_wide(self):
        """
        PURPOSE: Tests the 'count_faces_per_roll' method of the Analyzer class on a wide dataframe by ensuring the length of the resulting dataframe is as expected.
            
        INPUT:
        none
        
        OUTPUT:
        none
        """
        die1 = Die(np.array(['a', 'b', 'c']))
        die2 = Die(np.array(['a', 'b', 'c']))
        die3 = Die(np.array(['a', 'b', 'c']))
        die2.change_weight('b', 3)
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(10)
        game_results_wide = game.show_results('wide')
            
        analyze_wide = Analyzer(game_results_wide)
        analyze_wide.count_faces_per_roll()
            
        actual = len(analyze_wide.val_counts_df)
        expected = 10
        self.assertEqual(actual, expected)
        
    def test_6_count_faces_per_roll_nar(self):
        """
        PURPOSE: Tests the 'count_faces_per_roll' method of the Analyzer class on a narrow dataframe by ensuring the length of the resulting dataframe is as expected.
        """
        die1 = Die(np.array(['a', 'b', 'c']))
        die2 = Die(np.array(['a', 'b', 'c']))
        die3 = Die(np.array(['a', 'b', 'c']))
        die2.change_weight('b', 3)
        dice = [die1, die2, die3]
            
        game = Game(dice)
        game.play(10)
        game_results_nar = game.show_results('narrow')
            
        analyze_nar = Analyzer(game_results_nar)
        analyze_nar.count_faces_per_roll()
            
        actual = len(analyze_nar.val_counts_df)
        expected = 10
        self.assertEqual(actual, expected)
            
    
if __name__ == '__main__':
    unittest.main(verbosity=2)