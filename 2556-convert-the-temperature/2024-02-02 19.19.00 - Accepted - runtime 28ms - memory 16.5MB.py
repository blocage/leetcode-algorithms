class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [round(celsius + 273.15, 5), round(celsius * 1.8 + 32, 5)]