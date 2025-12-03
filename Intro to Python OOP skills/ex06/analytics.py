import logging
import requests

from random import randint
from config import TELEGRAM_API_URL, TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN


logging.basicConfig(
    filename='analytics.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    encoding='utf-8'
)

logging.info('The message is written to the file analytics.log')




class Research:
    def __init__(self, file_path):
        self.file_name = file_path
        logging.info(f'Research initialized with file: {file_path}')

    def file_reader(self, has_header=True):

        logging.info('Research.file_reader')
        try:
            with open(self.file_name, 'r') as f:
                lines = f.readlines()


            header = lines[0].strip().split(',')

            if header in [['0', '1'], ['1', '0']]:
                has_header = False
            data = []
            start_index = 1 if has_header else 0
            for line in lines[start_index:]:
                line = line.strip()
                if line:
                    values = line.split(',')
                    if len(values) != 2:
                        raise ValueError(f'Must contain exactly two values')
                    if not (values[0].strip() in ['0', '1'] and values[1].strip() in ['0', '1']):
                        raise ValueError(f'Values must be 0 or 1')
                    if values[0].strip() == values[1].strip():
                        raise ValueError(f'Values cannot be the same')
                    data.append([int(values[0]), int(values[1])])
            logging.info('Research.file_reader - Success')
            return data
        except Exception as e:
            logging.error(f'Research.file_reader - Error: {e}')
            raise

    def send_telegram_message(self, success=True):
        logging.info('Research.send_telegram_message')
        if success:
            message = "The report has been successfully created"
        else:
            message = "The report hasn't been created due to an error"

        try:
            payload = {
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message
            }
            response = requests.post(TELEGRAM_API_URL, data=payload, timeout=10)
            response.raise_for_status()
            logging.info('Research.send_telegram_message - Success')
            return True
        except Exception as e:
            logging.error(f'Research.send_telegram_message - Error: {e}')
            return False

class Calculations:
    def __init__(self, data):
        self.data = data
        logging.info(f'Calculations initialized with {len(data)} data points')

    def counts(self):
        logging.info('Calculations.counts')

        head = 0
        tails = 0
        for row in self.data:
            head += row[0]
            tails += row[1]

        logging.info('Calculations.counts - Success')
        return head, tails

    def fractions(self):
        logging.info('Calculations.fractions')

        head, tails = self.counts()
        result = head + tails
        if result == 0:
            return 0, 0
        head_percent = (head/result)*100
        tails_percent = (tails/result)*100

        logging.info('Calculations.fractions - Success')
        return head_percent, tails_percent

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)
        logging.info('Analytics initialized')

    def predict_random(self, NUM_OF_STEPS):
        logging.info('Analytics.predict_random')

        result = []
        for _ in range(NUM_OF_STEPS):
            num = randint(0, 1)
            if num == 0:
                result.append([0, 1])
            else:
                result.append([1, 0])

        logging.info('Analytics.predict_random - Success')
        return result

    def predict_last(self):
        logging.info('Analytics.predict_last')
        if not self.data:
            logging.info('Analytics.predict_last - No data')
            return None
        result = self.data[-1]
        logging.info('Analytics.predict_last - Success')
        return result

    def save_file(self, data, file_name, extension='.txt'):
        logging.info('Analytics.save_file')
        full_file_name = file_name + extension
        try:
            with open(full_file_name, 'w', encoding='utf-8') as f:
                f.write(str(data))
            print(f"File {full_file_name} saved successfully.")
            success = True
            logging.info('Analytics.save_file - Success')
        except Exception as e:
            print(f'Error while saving {e}')
            logging.error(f'Analytics.save_file - Error: {e}')
            success = False
        return success