# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Initialize a county list and county dictionary
county_options = []
county_votes = {}
#Initialize an empty string that will hold the county name for the couty with the largest turnout and a variable to hold the number of votes
largest_turnout_county = ""
largest_turnout_count = 0
largest_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    #Write a for loop that gets the county name for each row
    for row in file_reader:
        county_name = row[1]
        #If county name does not match an existing county, add it to the list
        if county_name not in county_options:
            county_options.append(county_name)
            # Write a script that initialize the county vote to 0
            county_votes[county_name] = 0
        #Write a script that adds a vote to the county's vote count as youre looping through the rows
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results, end="")
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    print ("-------------------------")
    #Write a repetition statement to get the county from the county dictionary
    for county_name in county_votes:
        #Intialize a varialbe to hold the county's votes as they are retrieved from the county votes dictionary
        countys_votes = county_votes[county_name]
        #Write a script that calculates the county's vote as a percentage of the total votes
        county_percentage = float(countys_votes) / float(total_votes) * 100
        #Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line
        county_results = (
            f"{county_name}: {county_percentage:.1f}% ({countys_votes:,})\n"
        )
        print (county_results, end="")
        # Save county results to the text file.
        txt_file.write(county_results)
        #Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables
        if (countys_votes > largest_turnout_count) and (county_percentage > largest_county_percentage):
            largest_turnout_count = countys_votes
            largest_turnout_county = county_name
            largest_county_percentage = county_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary, end="")
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    #Write a print statement that prints out the county with the largest turnout
    largest_county_summary = (
        f"Largest County Turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(largest_county_summary, end="")
    #Save the largest county turnout to the text file
    txt_file.write(largest_county_summary)