import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")  
file_to_output = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 
candidate_names = []
candidate_votes = {}
candidate_winner = 0
winning_candidate =''

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name =row[2]

        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        if votes > candidate_winner :
            candidate_winner  = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

