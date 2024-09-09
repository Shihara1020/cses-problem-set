# Read the input
n = int(input())
projects = []
for _ in range(n):
    start, end, reward = map(int, input().split())
    projects.append((end, start, reward))
projects.sort()
best_total_reward = 0
dp = {0: 0}  # {end: totalRewardSoFar}
for project in projects:
    end, start, reward = project

    # Find the largest end time that is <= start
    keys = list(dp.keys())
    it = max([k for k in keys if k < start])

    # Calculate the total reward if this project is selected
    total_reward = dp[it] + reward
    best_total_reward = max(best_total_reward, total_reward)

    # Update the dp table for the current end time
    dp[end] = best_total_reward

print(best_total_reward)

