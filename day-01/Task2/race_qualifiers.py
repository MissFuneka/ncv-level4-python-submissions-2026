#initializing the variables
qualified = 0
number_of_runners= 0
winner = ""
best_time = 0
qualifiedList = []

while True:
    # 1. Enter runners name
    # 2. Enter the time ran
    # 3. use x as sentinel
    
    name = input("\nEnter runner's name (x to stop): ")
    if name.lower() == "x":
        break
    time = input("Enter time ran in minutes and seconds (mm:ss): ")
    
    # check the right format is used for time
    timeString = time.split(":")

    if len(timeString) == 2 and timeString[0].isdigit() and timeString[1].isdigit():

        minutes = int(timeString[0])
        seconds = int(timeString[1])

        if seconds < 60:

            # As per hint convert time into seconds
            total_seconds = minutes * 60 + seconds
            number_of_runners = number_of_runners+ 1

            # Check out which runners qualified (25 minutes or less)
            if total_seconds <= 1500:
                qualified = qualified + 1
                qualifiedRunner = name
                qualifiedList.append(qualifiedRunner)                
                print(qualifiedRunner," has qualified" )
            else:
                qualifiedRunner = name
                print(qualifiedRunner," has not qualified" )

            # Find the winner (lowest time)
            if total_seconds < best_time or winner == "":
                best_time = total_seconds
                winner = name

        else:
            print("Invalid time! check seconds entered. 59 seconds or less ")

    else:
        print("Invalid time! Athlete ignored.")


# Display results
print("\n ======= RACE RESULTS =======")
if winner == "":
    print("No runners entered.")
else:
    win_minutes = best_time // 60
    win_minutes = str(win_minutes)
    
    win_seconds = best_time % 60
    win_seconds = str(win_seconds)

    print("\nWinner:", winner.capitalize(), " Time",win_minutes,"minutes :",win_seconds, "seconds")

print("\nQualified:", qualified,"of",number_of_runners)
# number_of_runners = int(number_of_runners)
if number_of_runners > 0:
    print("The following runners qualified")
    for runner in qualifiedList:
        print(runner.capitalize())
