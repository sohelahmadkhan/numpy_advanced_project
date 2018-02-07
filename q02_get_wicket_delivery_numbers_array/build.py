#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):

    player_got_out = ipl_matches_array[:,11][[ipl_matches_array[:,20] == player]]
    #print type(player)
    #print type(player_got_out)
    return player_got_out


print get_wicket_delivery_numbers_array('ST Jayasuriya')
