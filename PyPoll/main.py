import os
import csv

# Path to the election data CSV file
pypoll_csv = os.path.join("C:\\Users\\61433\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
with open(pypoll_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)  # Skip the header row
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        total_votes = total_votes + 1 
        candidate_name = row[2]
        
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Print the total number of votes
print(f'Total votes: {total_votes}')

# Print the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes} votes)')

# Determine the winner by finding the candidate with the maximum votes
winner = max(candidate_votes, key=candidate_votes.get)
    
# Print the winner of the election
print(f'Winner: {winner}')

# Path to the output text file
output_path = "C:\\Users\\61433\\Desktop\\python-challenge\\PyPoll\\analysis\\election_results.txt"
# Prepare the results
results = [
    "Election Results\n",
    "-------------------------\n",
    f"Total Votes: {total_votes}\n",
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
]
# Add each candidate's results to the output
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")

# Write the results to the text file
with open(output_path, "w") as txt_file:
    txt_file.writelines(results)
