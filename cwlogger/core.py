import datetime
import time

import boto3


class CWLogger:
    def __init__(self, log_group):
        self.log_group = log_group
        self.start_time = int(datetime.datetime.today().timestamp()) * 1000
        self.client = boto3.client('logs')
        self.wait_time = 2

    def __tail_logger(self):
        events = []

        while True:
            logs = self.client.filter_log_events(
                logGroupName=self.log_group,
                startTime=self.start_time
            )

            for event in logs.get('events', []):
                if event['eventId'] not in events:
                    events.append(event['eventId'])
                    yield event

    def tail(self):
        try:
            for event in self.__tail_logger():
                print(event['message'])
                time.sleep(self.wait_time)
        except KeyboardInterrupt:
            print('Shutdown by user.')
            exit()