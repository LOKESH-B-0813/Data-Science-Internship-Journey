# EVM Voting Machine

bjp = 0
admk = 0
dmk = 0
tvk = 0

print("===== EVM VOTING MACHINE =====")
print("1. BJP")
print("2. ADMK")
print("3. DMK")
print("4. TVK")

voters = int(input("Enter number of voters: "))

for i in range(voters):
    print(f"\nVoter {i+1}")
    vote = int(input("Cast your vote (1-4): "))

    if vote == 1:
        bjp += 1
        print("Vote recorded for BJP")
    elif vote == 2:
        admk += 1
        print("Vote recorded for ADMK")
    elif vote == 3:
        dmk += 1
        print("Vote recorded for DMK")
    elif vote == 4:
        tvk += 1
        print("Vote recorded for TVK")
    else:
        print("Invalid Vote!")

print("\n===== ELECTION RESULTS =====")
print("BJP Votes :", bjp)
print("ADMK Votes:", admk)
print("DMK Votes :", dmk)
print("TVK Votes :", tvk)

# Finding winner
max_votes = max(bjp, admk, dmk, tvk)

if max_votes == bjp:
    winner = "BJP"
elif max_votes == admk:
    winner = "ADMK"
elif max_votes == dmk:
    winner = "DMK"
else:
    winner = "TVK"

print("\nWinner of the Election:", winner)
print("Total Votes Received:", max_votes)
