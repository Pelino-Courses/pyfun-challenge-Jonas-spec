import datetime
def date_difference(date1: str, date2: str) -> int:
    try:
        d1 = datetime.datetime.strptime(date1, "%Y-%m_%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        delta = d2 - d1
        return delta.days
    except ValueError as ve:
        raise ValueError("PLease provide dates in 'YYY-MM-DD' format.") from ve
    if __name__ == "__main__":
        try:
            print(date_difference("20203-04-01","2023-04-10"))
        except ValueError as e:
            print(f"Error: {e}")