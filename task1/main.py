import heapq

nums = [4, 10, 3, 5, 1]
heapq.heapify(nums)
total_cost = 0

while len(nums) > 1:
    # Витягти два найкоротші кабелі
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)

    cost = x + y
    total_cost += cost

    heapq.heappush(nums, cost)

print("Загальні витрати на об'єднання кабелів:", total_cost)
