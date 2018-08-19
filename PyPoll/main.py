import os
import csv

csvpath = os.path.join('election_data.csv')

total_vote=0
candidates_choose={}
winner_vote=0



with open(csvpath, newline='',encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    for row in csvreader:

        total_vote= total_vote + 1
        candidates_name=row[2]

        if candidates_name in candidates_choose:
            candidates_choose[candidates_name]+= 1
        else:
            candidates_choose[candidates_name] = 1        
        
        
#output_file = os.path.join("output.csv")
#with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    
    #election_results=(
        #f"Election Resutls\n"
        #f"----------------------------\n"
        #f"Total Votes: + {total_vote}\n"
        #f"----------------------------\n")
    #print(election_results)
    #writer = csv.writer(csv_file)


    for candidates_name in candidates_choose:

        percentage =candidates_choose[candidates_name]/total_vote


    #print(candidates_name + ": " + str(round((percentage * 100),2)) + 
   #"% (" + str(total_vote) + ")")

    for candidates_name in candidates_choose:
        if candidates_choose[candidates_name] > winner_vote:
            winner = candidates_name
            winner_vote = candidates_choose[candidates_name]

   
    election_results=(
        f"Election Resutls\n"
        f"----------------------------\n"
        f"Total Votes: + {total_vote}\n"
        f"----------------------------\n"
        f"{candidates_name}:"+ str(round((percentage * 100),2)) + "% (" 
        + str(total_vote) + ")"+ "\n"
        f"----------------------------\n"
        f"The Winner is: " + winner+ "\n"
        f"----------------------------\n" )

    print(election_results)


output_file = os.path.join("output.csv")
with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(election_results)




    


