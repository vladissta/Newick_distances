#!/usr/bin/env python3

import parser
import calculate_distances

# FILENAME = 'newick.tree'
FILENAME = 'animals.tree'

graph = parser.parse_newick(FILENAME)
distances = calculate_distances.calculate_distances(graph)

table = [[''] + list(distances.keys())]

n = 0
for name, dists in distances.items():
    table.append([name] + list(dists.values())[:n] + ['-'] + list(dists.values())[n:])
    n += 1

for row in table:
    print(('|' + '{:^10} |' * (n + 1)).format(*row))
