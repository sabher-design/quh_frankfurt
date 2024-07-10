# coding=utf-8
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

import pandas as pd
import csv


class Constants(BaseConstants):
    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 DESIGN SETUP                                                  #
    #                                                                                                               #
    # ============================================================================================================= #

    # NUMBER OF PLAYERS =========================================================================== #
    #   Please specify how many players per market will participate.                                #
    players_per_group = 4

    # VALUATION VECTORS =========================================================================== #
    #   Different player types can have different valuation vectors for resources. Set the          #
    #   valuation vectors for each type and resource (Please keep in mind that the number of value  #
    #   vectors has to be a number that is completely divisible by the variable                     #
    #   "players_per_group"). E.g., if the market has three types and six resources, set the first  #
    #   six values within the list for a type to a number. Please stick to the scheme below.        #
    #   This app supports up to 10 types and 10 resources. Types are generated by id_in_group.      #
    #   This means that if you have 4 players and 2 types, players 1 and 2 are Type1, and           #
    #   players 3 and 4 are Type2.                                                                  #

    val7_t1 = [8, 18, 13, 3]
    val7_t2 = [13, 18, 3, 8]
    val7_t3 = [18, 8, 13, 3]
    val7_t4 = [13, 18, 3, 8]
# Set vectors for multiple types in the following way:
# valuations_t2 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
# valuations_t3 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
# valuations_t4 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
# ...

# PRIORITIES OF RESOURCES OVER PARTICIPANTS =================================================== #
#   Since this app models only the proposing side as active players, the priorities of the      #
#   resources over the players have to be specified. Please assign a priority vector for every  #
#   resource. The length of each vector has to be equal to the number of players specified      #
#   above. The structure is [<Player with Priority 1>, <Player with Priority 2>, ...]           #

    #prio7_r1 = [1, 2, 3, 4]
    #prio7_r2 = [1, 2, 3, 4]
    #prio7_r3 = [1, 2, 3, 4]
    #prio7_r4 = [1, 2, 3, 4]

    prio7_r1 = [3, 2, 1, 4]
    prio7_r2 = [4, 2, 1, 3]
    prio7_r3 = [1, 2, 4, 3]
    prio7_r4 = [2, 1, 4, 3]

# Set vectors for multiple resources in the following way:
#       priorities_r2 = [1, 2]
#       priorities_r3 = [1, 2]
#       ...

# RESOURCE CAPACITIES ========================================================================= #
#   Set the quota of players that each resource can carry. Fill in as many number as in the     #
#   valuation vectors.                                                                          #
    capacities = [1, 1, 1, 1]

# ============================================================================================================= #
#                                                                                                               #
#                                                 APPEARANCE SETTINGS                                           #
#                                                                                                               #
# ============================================================================================================= #

    # FRAMING ===================================================================================== #
    #   Here you can choose between a neutral framing (participants/resources) and a application    #
    #   framing (participants/schools).                                                             #
    application_framing = True

    # SHOW INSTRUCTIONS =========================================================================== #
    #   Should the instructions for the mechanism be included?                                      #
    instructions = False

    # SHOW EXAMPLE IN INSTRUCTIONS ================================================================ #
    #   If "instructions = True", should the instructions also include a minimal example of the     #
    #   mechanism in place?                                                                         #
    instructions_example = False

    # SHOW CONFIRM BUTTON ========================================================================= #
    #   If "confirm_button" is set to "True", players will have to confirm their inputs made on     #
    #   Decision.html to. This can be used to avoid accidental submission of the page.              #
    confirm_button = False

    # SHOW RESULTS ================================================================================ #
    #   Should a results screen be included? The results screen shows a summary of results of the   #
    #   market (i.e., preferences submitted, bids made, clearing bids, allotted resources), and the #
    #   final payoff for the player.                                                                #
    results = True

# ============================================================================================================= #
#                                                                                                               #
#                                                 INFORMATION SETTINGS                                          #
#                                                                                                               #
# ============================================================================================================= #

    # SHOW CAPACITIES ============================================================================= #
    #   If set to "True", the quota specified in "capacities" above will be shown to players on the #
    #   decision screen and in the instructions.                                                    #
    show_capacities = False

    # SHOW TYPES ================================================================================== #
    #   If "show_types" is set to "True", players will have a hint on the decision page and in the  #
    #   instructions that there are different types of players in the market. Only works if         #
    #   multiple type vectors have been specified above.                                            #
    show_types = True

    # SHOW OTHERS' VALUATIONS ===================================================================== #
    #   Should players see the other players' valuation profiles and on the decision page? Only     #
    #   works if "show_types" has been set to "True" above.                                         #
    show_val7 = True

    # SHOW RESOURCES' PRIORITIES ================================================================== #
    #   Should a player see the resources' priorities for her in the instructions and on the        #
    #   decision page?                                                                              #
    show_prio7 = False

####################################################################################################################
####################################################################################################################
# ------------------------------              DO NOT MODIFY BELOW HERE              ------------------------------ #
####################################################################################################################
####################################################################################################################

    capacities = [i for i in capacities if i is not None]
    nr_courses = len(capacities)

    val7_list = ["val7_t" + str(i) for i in range(1, 11)]
    val7_raw = []
    for i in val7_list:
        if i in locals():
            val7_raw.append(locals()[i])

    val7 = []
    for i in val7_raw:
        val7.append([j for j in i if j is not None])

    prio7_list = ["prio7_r" + str(i) for i in range(1, 11)]
    prio7_raw = []
    for i in prio7_list:
        if i in locals():
            prio7_raw.append(locals()[i])

    prio7 = []
    for i in prio7_raw:
        prio7.append([j for j in i if j is not None])

    nr_types = len(val7)

    name_in_url = "SHttc7_adv"
    num_rounds = 1