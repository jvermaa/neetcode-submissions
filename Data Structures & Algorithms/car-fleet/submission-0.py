class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        paired_up = [(p, s) for p, s in zip(position, speed)]

        paired_up.sort(reverse = True)

        sack = []

        for p, s in paired_up:
            sack.append((target-p)/s)

            if len(sack) > 1 and sack[-1] <= sack[-2]:
                sack.pop()
        
        return len(sack)