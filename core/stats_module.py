# core/stats_module.py
from collections import defaultdict
from core.db import load_all

def count_by_department():
    data = defaultdict(int)
    for p in load_all():
        data[p.department] += 1
    return dict(data)

def avg_gpa_by_department():
    sums = defaultdict(float)
    counts = defaultdict(int)
    for p in load_all():
        sums[p.department] += p.gpa
        counts[p.department] += 1
    averages = {}
    for dept in sums:
        averages[dept] = sums[dept] / counts[dept]
    return averages
