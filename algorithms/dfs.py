from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        frontier = [(initial, 0)]
        best_depth = {initial.tiles: 0}
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            state, depth = frontier.pop()
            if depth > best_depth[state.tiles]:
                continue
            if state.is_goal:
                result.solution = state
                result.depth = depth
                return result
            if depth >= self.depth_limit:
                continue

            result.nodes_expanded += 1
            for child in reversed(state.neighbors()):
                child_depth = depth + 1
                if child_depth < best_depth.get(child.tiles, float("inf")):
                    best_depth[child.tiles] = child_depth
                    frontier.append((child, child_depth))
                    result.nodes_generated += 1
            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
