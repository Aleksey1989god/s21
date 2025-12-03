import config

from analytics import Research, Calculations, Analytics
from config import num_of_steps, file_path

def main():
    try:
        research = Research(file_path)
        data = research.file_reader()
        calc = Calculations(data)
        head, tail = calc.counts()
        head_percent, tail_percent = calc.fractions()
        analytics = Analytics(data)
        predicts = analytics.predict_random(num_of_steps)
        predicted_heads = sum(p[0] for p in predicts)
        predicted_tails = sum(p[1] for p in predicts)

        report = config.text.format(
            total_observations=len(data),
            tails_count=tail,
            heads_count=head,
            tails_percent=tail_percent,
            heads_percent=head_percent,
            predicted_tails=predicted_tails,
            predicted_heads=predicted_heads,
            num_of_steps=num_of_steps
        )
        analytics.save_file(report, 'Report', '.txt')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()