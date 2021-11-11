import dateutil.parser as dparser


def change_date_format(dates):
    ls = list()
    for i in dates:
      if is_date_valid(i):
          ls.append(dparser.parse(i, fuzzy=True).date().strftime('%Y%m%d'))

    return ls

def is_date_valid(s):
    try:
        dparser.parse(s, fuzzy=True).date().strftime('%Y%m%d')
        return True
    except ValueError:
        return False
    else:
        return True

if __name__ == "__main__":
    dates = change_date_format(["2010/03/40", "15/12/2016", "11-15-2012", "20130720"])
    print(*dates, sep='\n')