import random
# Data in a consistent format
data = [
    {"name": "Cristiano Ronaldo", "follower_count": 630_000_000},
    {"name": "Lionel Messi", "follower_count": 500_000_000},
    {"name": "Neymar Jr.", "follower_count": 220_000_000},
    {"name": "Kylian Mbappé", "follower_count": 120_000_000},
    {"name": "Sergio Ramos", "follower_count": 65_000_000},
    {"name": "Mohamed Salah", "follower_count": 65_000_000},
    {"name": "Karim Benzema", "follower_count": 75_000_000},
    {"name": "Virgil van Dijk", "follower_count": 20_000_000},
    {"name": "Robert Lewandowski", "follower_count": 35_000_000},
    {"name": "Erling Haaland", "follower_count": 40_000_000},
    {"name": "Zlatan Ibrahimović", "follower_count": 60_000_000},
    {"name": "Ronaldinho", "follower_count": 75_000_000},
    {"name": "David Beckham", "follower_count": 85_000_000},
    {"name": "Marcelo", "follower_count": 65_000_000},
    {"name": "Paul Pogba", "follower_count": 60_000_000},
    {"name": "Virat Kohli", "follower_count": 273_000_000},
    {"name": "Sachin Tendulkar", "follower_count": 50_800_000},
    {"name": "MS Dhoni", "follower_count": 49_800_000},
    {"name": "Rohit Sharma", "follower_count": 44_100_000},
    {"name": "Hardik Pandya", "follower_count": 41_200_000},
    {"name": "Suresh Raina", "follower_count": 27_700_000},
    {"name": "AB de Villiers", "follower_count": 27_500_000},
    {"name": "KL Rahul", "follower_count": 22_700_000},
    {"name": "Yuvraj Singh", "follower_count": 20_700_000},
    {"name": "Jasprit Bumrah", "follower_count": 20_600_000},
    {"name": "Shikhar Dhawan", "follower_count": 19_400_000},
    {"name": "Suryakumar Yadav", "follower_count": 18_200_000},
    {"name": "Shubman Gill", "follower_count": 16_300_000},
    {"name": "Mohammed Shami", "follower_count": 16_000_000},
    {"name": "Rishabh Pant", "follower_count": 15_000_000},
    {"name": "Smriti Mandhana", "follower_count": 12_300_000},
    {"name": "Rashid Khan", "follower_count": 11_000_000},
    {"name": "Babar Azam", "follower_count": 6_000_000},
    {"name": "Shakib Al Hasan", "follower_count": 2_700_000},
]

# Display format
def format_data(account):
    return f"{account['name']} :"

# Logic to check guess
def check_answer(guess, a_count, b_count):
    return (guess == 'a' and a_count > b_count) or (guess == 'b' and b_count > a_count)

# Intro and logo
print("🏆 WELCOME TO HIGHER OR LOWER (CHAIN REACTION EDITION) 🏆")
print("Guess who has more followers. Let's go!\n")

# Score tracking and initial setup
score = 0
game_should_continue = True
account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
    account_b = random.choice(data)

# Game loop
while game_should_continue:
    print(f"\nCompare A: {format_data(account_a)}")
    print("🔛 VS 🔛")
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct and guess == "a":
        score += 1
        print(f"✅ Correct! Current Score: {score}")
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
    elif is_correct and guess == "b":
        score += 1
        print(f"✅ Correct! Current Score: {score}")
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
    else:
        game_should_continue = False
        print(f"❌ Wrong! Final Score: {score}")

