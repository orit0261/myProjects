import calendar
from datetime import datetime, timedelta

import datefinder
import pytz
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

email = 'orit0261@gmail.com'
my_zone = 'Asia/Jerusalem'


def build_calender():
    scopes = ['https://www.googleapis.com/auth/calendar']
    # Create authorization credentials from Credentials page in google console
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))
    credentials = pickle.load(open("token.pkl", "rb"))
    # load data from the user calendar
    service = build("calendar", "v3", credentials=credentials)
    return service


def search_calender(service, start, end):
    # calendarlist = a list with all the ids of the calendars I do query
    # calendar is the access token to google calendar API
    # build request json
    freebusy_query = {
        "timeMin": start.isoformat(),
        "timeMax": end.isoformat(),
        "timeZone": 'Asia/Jerusalem',
        "items": [{"id": email}]
    }
    # call freebusy API
    eventsResult = service.freebusy().query(body=freebusy_query).execute()
    # get events
    cal_dict = eventsResult[u'calendars']
    return cal_dict

    # for cal_name in cal_dict:
    #   print(cal_name, cal_dict[cal_name])

    # function for creating new meeting if free date


def create_event(service, start_time_str, summary, duration=1, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    start_time = None
    end_time = None
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    if start_time and end_time:
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': my_zone,
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': my_zone,
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        return service.events().insert(calendarId='primary', body=event).execute()
    else:
        return None


def main():
    service1 = build_calender()
    tz = pytz.timezone(my_zone)
    start1 = tz.localize(datetime(2022, 4, 27, 0))
    end1 = tz.localize(datetime(2022, 4, 27, 8))
    cal_dict1 = search_calender(service1, start1, end1)
    print(cal_dict1)
    if cal_dict1[email]['busy'] == list():
        print('date and time are available')
        create_event(service1, "15 may 9 PM", "date in TLV", 1, "business meet", 'TLV')
    else:
        print('date and time are not available')


if __name__ == "__main__":
    main()
