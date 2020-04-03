import datetime
import time
import cwlogger.date_parser as date_parser
import boto3


class CWLogger:
    __WAIT_TIME = 2
    LOG_LIMIT = 100

    def __init__(self, log_group, profile_name=None):
        botosession = boto3.Session(profile_name=profile_name)
        self.log_group = log_group
        self.start_time = int(datetime.datetime.now().timestamp()) * 1000
        self.end_time = int(datetime.datetime.now().timestamp()) * 1000
        self.client = botosession.client('logs')

    def __parse_time(self, delta_expr):
        delta = datetime.timedelta(**delta_expr).total_seconds()

        return int(datetime.datetime.now().timestamp() + delta) * 1000

    def __tail_logger(self):
        events = []
        filter_logs_kwargs = {
            'logGroupName': self.log_group,
            'startTime': self.start_time,
            'endTime': self.end_time,
            'limit': self.LOG_LIMIT
        }

        while True:
            response = self.client.filter_log_events(**filter_logs_kwargs)

            for event in response.get('events', []):
                if event['eventId'] not in events:
                    events.append(event['eventId'])
                    yield event

            if 'nextToken' in response:
                filter_logs_kwargs['nextToken'] = response['nextToken']
            else:
                yield None

    def get_logs(self, watch=False, **kwargs):
        if 'end' in kwargs:
            self.end_time = date_parser.DateParser(kwargs['end']).ts

        if 'start' in kwargs:
            self.start_time = date_parser.DateParser(kwargs['start']).ts

        for log in self.__tail_logger():
            if log is None:
                if watch:
                    time.sleep(self.__WAIT_TIME)
                    continue
                else:
                    break

            yield log
