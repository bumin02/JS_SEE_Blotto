# me = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
me = [1, 2, 11, 3, 4, 15, 22, 22, 17, 3]
# me = [1, 2, 11, 2, 2, 15, 22, 22, 20, 3]

f = "opponent_soldiers.txt"

"""This is a program to calculate the scores bewteen you and the opponent.
   This Python file will take in numerous combinations of enemy soldier allocations,
   and compute to see who has allocated their soldiers better. """

def get_scores(me, f):

    with open(f) as opponent:
        my_num_wins, total_games = 0, 0
        for opp_soldiers_list in opponent:
            my_max_consec_ls, opp_max_consec_ls = [], []
            my_points, opp_points = 0, 0
            my_max_losing, opp_max_losing = 0, 0
            opp = [eval(i) for i in opp_soldiers_list.split()]
            my_win_streak, opp_win_streak = 0, 0
            for i in range(len(opp)):
                if me[i] - opp[i] > 0:
                    my_points += i+1
                    my_win_streak += 1
                    opp_max_consec_ls.append(opp_win_streak)
                    opp_win_streak = 0
                    
                elif me[i] - opp[i] < 0:
                    opp_points += i+1
                    my_max_consec_ls.append(my_win_streak)
                    my_win_streak = 0
                    opp_win_streak += 1

            opp_max_consec_ls.append(opp_win_streak)
            my_max_consec_ls.append(my_win_streak)

            my_max_consec, opp_max_consec = max(my_max_consec_ls), max(opp_max_consec_ls)

            # if my_max_consec == 1 or opp_max_consec == 1:
            if my_max_consec == opp_max_consec:
                my_max_consec = 0
                opp_max_consec = 0
            else:
                my_max_losing = opp_max_consec
                opp_max_losing = my_max_consec
            
            my_points += 2*my_max_consec - my_max_losing
            opp_points += 2*opp_max_consec - opp_max_losing

            print("game number ", total_games+1)
            if my_points > opp_points:
                my_num_wins += 1
                print("WIN ::: MY POINTS:", my_points, ", OPPONENT POINTS:", opp_points)
            elif my_points < opp_points:
                print("LOSE ::: MY POINTS:", my_points, ", OPPONENT POINTS:", opp_points)
            else:
                print("TIE ::: ", my_points)
            
            total_games += 1

        print("\nmy win rate: ", my_num_wins / total_games, "\n")

get_scores(me, f)