num_of_steps = 28
file_path = '../../datasets/data.csv'

text = """We made {total_observations} observations by tossing a coin: {tails_count} were tails and {heads_count} were heads. 
The probabilities are {tails_percent:.2f}% and {heads_percent:.2f}%, respectively. 
Our forecast is that the next {num_of_steps} observations will be: {predicted_tails} tail(s) and {predicted_heads} head(s)."""