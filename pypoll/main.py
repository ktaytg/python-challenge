import os

import csv

# Datafile path to access the CSV
csvpath = os.path.join("C:/Users/katea/Columbia/Starter_Code/PyPoll/Resources/election_data.csv")

vote_count = {}
total_votes = 0


# -->>  The total number of votes cast
# -->>  A complete list of candidates who received votes
# -->>  The percentage of votes each candidate won
# -->>  The total number of votes each candidate won
# -->>  The winner of the election based on popular vote


with open(csvpath, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")    
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in vote_count:
            vote_count[candidate] +=1
            
        else:
                vote_count[candidate] = 1
                
        candidates = list(vote_count.keys())
        
        
        for candidate in candidates:
            votes = vote_count[candidate]
            percentage = (votes / total_votes) * 100
            print(f"{candidate}: {percentage:.2f}% ({votes})\n")
  

            winner = max(vote_count, key=vote_count.get)
            print(f"Winner: {winner}\n")

  
      
        # create print out file
        

with open("C:/Users/katea/Columbia/Starter_Code/PyPoll/Resources/output.txt", "w") as printoutfile: 
              
           printoutfile.write("Election Results\n")
           printoutfile.write("-----------------------\n")
           printoutfile.write(f"Total_Votes:  {total_votes}\n")
           printoutfile.write("------------------------\n") 
           
           for candidate in candidates:
               votes = vote_count[candidate]
               percentage = (votes / total_votes) * 100
               printoutfile.write(f"{candidate}: {percentage:.2f}% ({votes})\n")
               printoutfile.write("---------------------------\n")
              
               winner = max(vote_count, key=vote_count.get)
               printoutfile.write(f"Winner: {winner}\n")
               printoutfile.write("---------------------------\n")
