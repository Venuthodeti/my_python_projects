import random
data = [
{"Cristiano Ronaldo": 630_000_000},  # Instagram followers (approximate)
{"Lionel Messi": 500_000_000},
{"Neymar Jr.": 220_000_000},
{"Kylian Mbappé": 120_000_000},
{"Sergio Ramos": 65_000_000},
{"Mohamed Salah": 65_000_000},
{"Karim Benzema": 75_000_000},
{"Virgil van Dijk": 20_000_000},
{"Robert Lewandowski": 35_000_000},
{"Erling Haaland": 40_000_000},
{"Zlatan Ibrahimović": 60_000_000},
{"Ronaldinho": 75_000_000},
{"David Beckham": 85_000_000},
{"Marcelo": 65_000_000},
{"Paul Pogba": 60_000_000},
{"Virat Kohli": 273_000_000},
{"Sachin Tendulkar": 50_800_000},
{"MS Dhoni": 49_800_000},
{"Rohit Sharma": 44_100_000},
{"Hardik Pandya": 41_200_000},
{"Suresh Raina": 27_700_000},
{"AB de Villiers": 27_500_000},
{"KL Rahul": 22_700_000},
{"Yuvraj Singh": 20_700_000},
{"Jasprit Bumrah": 20_600_000},
{"Shikhar Dhawan": 19_400_000},
{"Suryakumar Yadav": 18_200_000},
{"Shubman Gill": 16_300_000},
{"Mohammed Shami": 16_000_000},
{"Rishabh Pant": 15_000_000},
{"Smriti Mandhana": 12_300_000},
{"Rashid Khan": 11_000_000},
{"Babar Azam": 6_000_000},
{"Shakib Al Hasan": 2_700_000},
]
import random
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return f"{name}, a {descr}, from {country}"
print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")
from art import logo, vs
print(logo)
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")
guess = input("Who has more followers? Type 'A' or 'B': ").lower()
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
def check_answer(guess, a_followers, b_followers):
    """Checks if the user's guess is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
is_correct = check_answer(guess, a_follower_count, b_follower_count)
score = 0
if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
else:
    print(f"Sorry, that's wrong. Final score: {score}.")
game_should_continue = True
score = 0
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
print("\n" * 20)