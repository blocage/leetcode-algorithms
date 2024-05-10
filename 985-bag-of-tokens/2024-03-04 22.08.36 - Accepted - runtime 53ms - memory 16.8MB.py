class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = deque(sorted(tokens))
        score = 0
        while score or tokens:
            if len(tokens) == 1:
                score += tokens[0] <= power
                break
            
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            else:
                if score:
                    power += tokens.pop()
                    score -= 1
                else:
                    break
        
        return score