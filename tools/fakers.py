import time

def get_random_email() -> str:
    return f"test.{time.time()}@example.ru"

print(get_random_email())