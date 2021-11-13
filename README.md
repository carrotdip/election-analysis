# Election_Analysis

## Project Overview
### The purpose of this project was to complete the election audit of a local congressional election. The committee was interested in the determination of the winning candidate as well as the analysis of the county voting data. First, The total number of votes cast was calculated.
![text](https://github.com/carrotdip/election-analysis/blob/85572a51651c6850fecee412fd204709fa1536f6/Screen%20Shot%202021-11-12%20at%209.27.58%20PM.png)\
![text](https://github.com/carrotdip/election-analysis/blob/85572a51651c6850fecee412fd204709fa1536f6/Screen%20Shot%202021-11-12%20at%209.28.09%20PM.png)
### A list of candidates and their total vote counts was then created and stored in a dictionary. This was done by looping through the data, and creating a list of unique candidate names, and then counting each time that name appeared. 
![text](https://github.com/carrotdip/election-analysis/blob/ef125b66d415657d65b68664b46a37c69f6b9588/Screen%20Shot%202021-11-12%20at%209.33.16%20PM.png)\
![text](https://github.com/carrotdip/election-analysis/blob/ef125b66d415657d65b68664b46a37c69f6b9588/Screen%20Shot%202021-11-12%20at%209.33.36%20PM.png)
### The percentage of votes of each candidate were then calculated to determine the winner of the election based on popular vote. This was done by dividing the candidate votes by the total votes and multiplying by 100.
![text](https://github.com/carrotdip/election-analysis/blob/37140435c493d1d53831c80585c843991c228976/Screen%20Shot%202021-11-12%20at%209.36.02%20PM.png)
### The election committee was also interested in the turnout rates per county. A list of counties and their total vote counts were determined with the same methods for the candidates. 
![text](https://github.com/carrotdip/election-analysis/blob/a41f4b02774aa1226af08ec0a8ba579e3b50bf04/Screen%20Shot%202021-11-12%20at%209.37.33%20PM.png)\
![text](https://github.com/carrotdip/election-analysis/blob/a41f4b02774aa1226af08ec0a8ba579e3b50bf04/Screen%20Shot%202021-11-12%20at%209.37.45%20PM.png)
### The percentages of the county votes were also calculated with the same process as previously described to determine the county with the highest turnout.
![text](https://github.com/carrotdip/election-analysis/blob/076347881ad2d17832e96a41168d07ee5ce7bcb0/Screen%20Shot%202021-11-12%20at%209.39.38%20PM.png)
## Election-Audit Results
- The analysis of the data set showed that there were a total of 369,711 votes cast. The complete list of candidates included Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.
- Charles Casper Stockham received 85,213 votes, which was 23.0% of the total votes. 
- Diana DeGette received 272,892 votes, making up 73.8% of the total votes. 
- And finally, Raymon Anthony Doane received 11,606 votes, or 3.1% of the total votes. 
- The winner of the election was Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 
- The complete list of counties included Jefferson, Denver, and Arapahoe. 
- The Jefferson county had a total vote count of 38,855 votes, which made up 10.5% of the total votes. 
- Denver county submitted a total of 306,055 votes, or 82.8% of the toal votes. 
- Finally, Arapahoe had 24,801 votes, which made up 6.7% of the total votes. 
- Denver county had the highest turnout in his congressional election.

## Resources
- Data source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code 1.62.1

## Election-Audit Summary
### The script used in this analysis can easily be modified to determine the results of any election. Many aspects of the code can be rewritten to include more forms of analysis. For example, for a national election, the turnout by state can also be determined by re-writing the code used to form the list of unique candidates and counties, and subsequently determining the vote count for each state. If the data allows, the color of the state based on political preference (Republican - red, Democratic - blue) can also be determined by using nested for loops counting the votes based on politic preference by state, and subsequently modifying the decision statements used in this analysis to determine the color of the state.
