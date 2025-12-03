import config
import logging


from analytics import Research, Calculations, Analytics
from config import NUM_OF_STEPS, file_path



def main():
    logging.info('Start make_report.py')

    try:
        research = Research(file_path)
        data = research.file_reader()
        calc = Calculations(data)
        head, tail = calc.counts()
        head_percent, tail_percent = calc.fractions()
        analytics = Analytics(data)
        predicts = analytics.predict_random(NUM_OF_STEPS)
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
            num_of_steps=NUM_OF_STEPS
        )
        success = analytics.save_file(report, 'report', '.txt')
        research.send_telegram_message(success=success)

    except Exception as e:
        logging.error(f'Error occurred: {e}')
        success = False

    if success:
        logging.info('make_report.py - Success')
    else:
        logging.error('make_report.py - Failed')

    print("Program completed successfully!" if success else "Program failed!")


if __name__ == '__main__':
    main()