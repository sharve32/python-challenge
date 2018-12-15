import os
import csv

#Read csv
election_ds = "Resources/election_data.csv"

with open(election_ds, newline="") as election_data:
    reader = csv.reader(election_data, delimiter=',')
    next(reader)
    #Create list for the voting data
    poll_list = []
    #Create dictionaries for each candidate
    candidate_votes = {}
    candidate_perc = {}
    candidate_winner = {}
    
    #Count number of total votes
    for row in reader:
        poll_list.append(row)
    TotalVotes = len(poll_list)

    #Count number of votes for each candidate
    for vote in poll_list:
        candidate_name = vote[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    #Calculate vote percentage for each candidate
    for name in candidate_votes:
        candidate_perc[name] = (candidate_votes[name]*100)/TotalVotes

    candidate_win = ["Candidate",0]
    for name in candidate_perc:
        if candidate_win[1] < int(candidate_perc[name]):
            candidate_win[1] = candidate_perc[name]
            candidate_win[0] = name

#Set up new text file for analysis output
output = open("Resources/election_results.txt", 'w+')

#Print to terminal
print(f"Election Results\n")
print(f"-------------------------------\n")
print(f"Total Votes = {TotalVotes}")
print(f"-------------------------------\n")
#Print to external text file
output.write(f"Election Results\n")
output.write(f"-------------------------------\n")
output.write(f"Total Votes = {TotalVotes}\n")
output.write(f"-------------------------------\n")

#Print vote outcomes for each candidate
for name in candidate_votes:
    candidate_perc[name] = '{:.3f}%'.format(candidate_perc[name])
    print(f"{name}: {candidate_perc[name]} ({candidate_votes[name]}) \n")
    output.write(f"{name}: {candidate_summary[name]} \n")

#Print winner to terminal
print(f"-------------------------------\n")
print(f"Winner: {candidate_win[0]} \n")
print(f"-------------------------------\n")
#Print winner to document
output.write(f"-------------------------------\n")
output.write(f"Winner: {candidate_win[0]} \n")
output.write(f"-------------------------------\n")

#Close relative external documents
output.close()
election_data.close()