import cProfile, pstats, io
from pstats import SortKey

profiler = cProfile.Profile()
profiler.enable()

def fib_list(n):
    if n < 2:
        return n
    sequence = [0, 1]
    profiler.enable()
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    profiler.disable()
    return sequence[n]

fib_list(300)

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats = stats.sort_stats(SortKey.CUMULATIVE)
stats.print_stats()
print(stream.getvalue())