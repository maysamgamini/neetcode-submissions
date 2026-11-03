class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _nums = {}
        for n in nums:
            _nums[n] = _nums.get(n,0) + 1
        heap = []
        for v, f in _nums.items():
            heapq.heappush(heap, (f, v))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
        