from collections import defaultdict

session_usage = defaultdict(int)

def track_session(user_id: str):
    session_usage[user_id] += 1
    return session_usage[user_id]
