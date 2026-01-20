class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        import math
        
        n = len(damage)
        
        # Calculate time to kill each enemy (ceil(health[i] / power))
        time_to_kill = [(health[i] + power - 1) // power for i in range(n)]
        
        # Create list of (damage, time_to_kill, index)
        enemies = [(damage[i], time_to_kill[i], i) for i in range(n)]
        
        # Sort by damage/time ratio in descending order
        # If we kill enemy i before j, the cost difference is:
        # damage[j] * time[i] vs damage[i] * time[j]
        # Kill i first if damage[i] / time[i] > damage[j] / time[j]
        # i.e., damage[i] * time[j] > damage[j] * time[i]
        
        enemies.sort(key=lambda x: x[0] / x[1], reverse=True)
        
        total_damage = 0
        time_elapsed = 0
        
        for dmg, ttk, idx in enemies:
            time_elapsed += ttk
            total_damage += dmg * time_elapsed
        
        return total_damage