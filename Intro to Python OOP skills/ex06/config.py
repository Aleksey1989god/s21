NUM_OF_STEPS = 28
file_path = '../../datasets/data.csv'
TELEGRAM_BOT_TOKEN = '5586469653:AAHF4JB8DQYgDQza5a7E_c7NJgORCnnxKa4'
TELEGRAM_CHAT_ID = '408164860'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

text = """We made {total_observations} observations by tossing a coin: {tails_count} were tails and {heads_count} were heads. 
The probabilities are {tails_percent:.2f}% and {heads_percent:.2f}%, respectively. 
Our forecast is that the next {num_of_steps} observations will be: {predicted_tails} tail(s) and {predicted_heads} head(s)."""