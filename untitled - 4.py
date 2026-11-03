import time

items = [
    f"Item{i}:Rs{i % 50}"
    for i in range(200000)
]


def build_plus(parts):

    text = ""

    for p in parts:
        text += p + ";"

    return text


def build_join(parts):

    return ";".join(parts) + ";"


def measure(function, data):

    times = []

    for i in range(3):

        start = time.perf_counter()

        result = function(data)

        end = time.perf_counter()

        times.append(end - start)

    average = sum(times) / 3

    return times, average


for size in [1000, 10000, 200000]:

    data = items[:size]

    plus_times, plus_avg = measure(build_plus, data)

    join_times, join_avg = measure(build_join, data)

    print("\nNumber of lines:", size)

    print("Plus times:", plus_times)
    print("Plus average:", plus_avg)

    print("Join times:", join_times)
    print("Join average:", join_avg)

    print("Same output:", build_plus(data) == build_join(data))