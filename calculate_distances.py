def process_node(node_from, field_of_search, graph):
    dist_dict = {}
    node_distance = graph[field_of_search][node_from]
    _inner_dict = graph[field_of_search]

    for node_inner, dist_inner in _inner_dict.items():  # iterating inside parent node

        if node_inner == node_from:
            continue

        if node_inner.startswith('Node_'):
            dist_dict.update((x, round(y + node_distance, 6)) for x, y in \
                             process_node(field_of_search, node_inner, graph).items())
        else:
            dist_dict[node_inner] = round(node_distance + dist_inner, 6)

    return dist_dict


def calculate_distances(graph):
    dists_all_leaves = {}

    for field_of_search, inner_dict in graph.items():  # node from "list" of nodes

        for leaf_main, dist_main in inner_dict.items():  # node to search distance from
            if leaf_main.startswith('Node_'):
                continue
            else:
                dists_all_leaves[leaf_main] = process_node(leaf_main, field_of_search, graph)

    return dists_all_leaves
