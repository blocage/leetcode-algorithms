class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        priority_queue<int> pq;
        int d, i;
        for(i=0; i < heights.size() - 1; i++){
            d = heights[i] - heights[i + 1];
            if (d < 0) pq.push(d);
            if (pq.size() > ladders){
                bricks += pq.top();
                pq.pop();
            }
            if (bricks < 0) return i;
        }
        return heights.size() - 1;
    }
};