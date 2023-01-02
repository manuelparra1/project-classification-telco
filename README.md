
Telco Customer Churn
Project Description

The Telco company has been losing customers and does not know why. Using the account information for each customer. I will compare different services that each customer pays for. A service or customer data could potentially increase or decrease the chance that a customer will churn.
Project Goal

    Find drivers of churn
    User drivers to create ML models

Initial Thoughts

My initial hypothesis is that drivers of churn will be descriptions of customers that isolate them in groups with higher likelihood of leaving the company.
The Plan

    Aquire data from SQL database

    Aquire data from SQL database

    Prepare data
        Left Join additional customer info to customers table
        Drop Redundant Columns

    Explore data in search of drivers of upsets
        Answer the following initial questions
            How often does churn occur?
            Does gender & total charge affect churn?
            Does join date affect churn?
            Does total addons affect churn?
            Does total deviation from average of total_charges affect churn?
            Does having tech support and being a senior citizen effect churn?
            Does being a senior citizen affect churn?
            Is tenure important driving churn?
            Is paperless_billing, payment_type related?
            Does having dependents & multiple_lines correlate to churn?

    Develop a Model to predict churn
        Use drivers identified in explore to build predictive models of different types
        Evaluate models on train and validate data
        Select the best model based on highest accuracy
        Evaluate the best model on test data

    Draw conclusions

Data Dictionary
Feature 	Definition
Churn 	True or False, The game's result is reflected in each player's rating
Winning Pieces 	The color of pieces the winning player was moving
White Rating 	Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess
Black Rating 	Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess
Rating Difference 	The difference in rating between the players in the game
Game Rating 	The average rating of the two players in the game
Lower Rated White 	True or False, The lower rated player is moving the white pieces
Opening Name 	The name of the opening played in the game
Time Control Group 	The amount of time allotted to each player to make their moves, Standard (60 min or more), Rapid (30 - 15 min), Blitz (5 - 3 min), or Bullet (2 or less), Other (any other time limit)
Upset (Target) 	True or False, The lower rated player won the game
Additional Features 	Encoded and values for categorical data and scaled versions continuous data
Instructions?
Steps to Reproduce

    Clone this repo.
    Acquire the data from Codeup SQL Database
    Put the data in the file containing the cloned repo.
    Run notebook.

Takeaways and Conclusions

    Upsets occur in 1/3 of games
    In games where the lower rated player moves first there is a 4% greater chance of an upset
    Games that are rated have a 3% higher chance of an upset
    Games with a "quick" time control (30 min or less) have about a 1 in 3 chance of upset
    Games with a "slow" time control (60 min or more) have about a 1 in 5 chance of upset
    The mean rating of players in a game is not a driver of upsets
    The difference in player rating is a driver of upsets
    A player's choice of opening is a driver of upsets, however its influence is complicated and I would need more time to discover what role it plays

Recommendations

    To increase the skill intensity of a game add to the length of time players are able to consider their moves
    Based on the data longer time controls make it less likely for a less skilled player to beat a more skilled player

