class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        for i in range(l := len(flowerbed)):
            if flowerbed[i] == 0 and flowerbed[max(i - 1, 0)] == 0 and flowerbed[min(i + 1, l - 1)] == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True
        
        return False