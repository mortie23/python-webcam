from datetime import datetime, timedelta

def timeminute():
    return (datetime.now() + (datetime.min - datetime.now()) % timedelta(minutes=1)).strftime("%Y%m%d-%H%M")
