print("Hello World")
print()
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)

print()

#Creating lists
counties = ["Arapahoe", "Denver", "Jefferson"]
#list() opens a new list?
#lists are mutable (able to be changed)
my_list = list()
print(counties)
counties[0]
len(counties)
#insert a new key at a certain position, print to check work
counties.insert(2,"El Paso")
print(counties)
#remove a specific key in the list, 3 = 4th item, print to check work
counties.pop(3)
print(counties)
#inserting El Paso at the 2nd position in the list, print to check work
counties.insert(1,"El Paso")
print(counties)
#removing the 1st key, or Arapahoe, and printing to check
counties.pop(0)
print(counties)
counties[2] = "Denver"
counties[0] = "El Paso"
print(counties)
#adding Arapahoe to the end of the list, print to check
counties.append("Arapahoe")
print(counties)
print()
#creating a tuple 
#tuples are immutable, or unable to be changed
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
print(counties_tuple)
#find the number of items in the tuple
print(len(counties_tuple))
len(counties)
print()
#defining counties dictionary
#creating a dictionary = {key:value}
counties_dict = {"Arapahoe" : 422829, "Denver": 463353, "Jefferson":432438}
#printing dictionary
print(counties_dict)
#printing length of dictionary = 3
print(len(counties_dict))
#print all the items in the counties_dict
print(counties_dict.items())
print()
#if-else statements
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
print()
for county in counties:
    print(county)   
for i in range(len(counties)):
    print(counties[i])
for county in counties_dict.keys():
    print(county)
print()
for voters in counties_dict.values():
    print(voters)
print()
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
print()
for key, value in counties_dict.items():
    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)
print()
for key, value in counties_dict.items():
    print((str(key))+" county has "+(str(value))+" registered voters.")
#WHY DOES THIS NOT WORK !!!!!!
for key, value in counties_dict.items():
    #print(f"{key} county has {value} registered voters.")


    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
             {"county":"Denver", "registered_voters": 463353},
             {"county":"Jefferson", "registered_voters": 432438}]
#print each dictionary using a simple loop
for county_dict in voting_data:
    print(county_dict)
#Use range f(x) to print each dictionary in voting_data
for i in range(len(voting_data)):
      print(voting_data[i])
print()
#using nested for loop to retrieve only the values from each dictionary in the list of dicts
#for loop to retrieve each dictionary
for county_dict in voting_data:
    #nested for loop to use the values() method on the variable county.dict
    for value in county_dict.values():
        print(value)
#to retrieve the registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
#to list the county names from the dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#Using F-strings
#f-strings begin with an f, followed by a string contained within quotes
#curly braces are used to add variables or expressions to the f-string
    my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
#using an f-string
#print(f"I received {my_votes/total_votes*100}% of the total votes.")
print()
#
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)
print()
#General format for numbers in an f-string
#f'{value:{width}.{precision}}'
#In the format, the width specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.
#The precision indicates the number of decimal places to format the value. For example, to format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format".
#When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.
f'{value:{width},.{precision.2f}}'
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")