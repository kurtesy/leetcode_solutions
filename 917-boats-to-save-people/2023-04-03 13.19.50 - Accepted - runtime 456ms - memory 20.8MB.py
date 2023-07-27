class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_people = sorted(people)
        len_people = len(people)
        boats = 0
        light = 0
        heavy = len_people - 1
        while light <= heavy:
            total = sorted_people[light] + sorted_people[heavy]
            if total > limit:
                heavy-=1
                boats+=1
            else:
                light+=1
                heavy-=1
                boats+=1
        return boats
        