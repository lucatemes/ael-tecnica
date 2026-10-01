class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        best = 0

        while left < right:
            # largura = distância entre as duas paredes
            width = right - left

            # a água é limitada pela parede menor
            current = width * min(height[left], height[right])

            best = max(best, current)

            # descarta a parede menor e pula duplicatas/menores na mesma direção
            # (largura só diminui, então só vale parar numa parede maior que a atual)
            if height[left] < height[right]:
                h = height[left]
                while left < right and height[left] <= h:
                    left += 1
            else:
                h = height[right]
                while left < right and height[right] <= h:
                    right -= 1

        return best


# --- testes ---
print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # esperado: 49
print(Solution().maxArea([1, 1]))                          # esperado: 1
print(Solution().maxArea([4, 3, 2, 1, 4]))                # esperado: 16
