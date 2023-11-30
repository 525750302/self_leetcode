
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        forbidden = {x for x, y in zip(fronts, backs) if x == y}
        return min((x for x in fronts + backs if x not in forbidden), default=0)