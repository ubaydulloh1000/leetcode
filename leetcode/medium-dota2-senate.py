from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiants = deque()
        dires = deque()
        
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                radiants.append(i)
            else:
                dires.append(i)
        
        while radiants and dires:
            radiant = radiants.popleft()
            dire = dires.popleft()

            n += 1
            if radiant < dire:
                radiants.append(n)
            else:
                dires.append(n)

        return "Dire" if dires else "Radiant"



def main():
    senate = "RDDRDDRRR"
    print(Solution().predictPartyVictory(senate))


if __name__ == '__main__':
    main()
