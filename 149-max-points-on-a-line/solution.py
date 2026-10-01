from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        result = 2

        for i in range(n):
            # hashmap: slope -> quantos pontos compartilham essa inclinação com o ponto i
            slopes = {}
            duplicates = 0  # pontos idênticos ao ponto i

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # mesmo ponto — conta separado, entra em qualquer linha
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # representa a inclinação como fração irredutível (dy, dx)
                # evita erro de ponto flutuante usando inteiros
                if dx == 0:
                    slope = (1, 0)  # linha vertical
                elif dy == 0:
                    slope = (0, 1)  # linha horizontal
                else:
                    # normaliza o sinal: denominador sempre positivo
                    if dx < 0:
                        dx, dy = -dx, -dy
                    divisor = gcd(abs(dy), abs(dx))
                    slope = (dy // divisor, dx // divisor)

                slopes[slope] = slopes.get(slope, 0) + 1

            # +1 (ponto i) + duplicates (pontos iguais a i)
            if slopes:
                result = max(result, max(slopes.values()) + 1 + duplicates)
            else:
                result = max(result, 1 + duplicates)

        return result


# --- testes ---
print(Solution().maxPoints([[1,1],[2,2],[3,3]]))            # esperado: 3
print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # esperado: 4
print(Solution().maxPoints([[0,0],[1,1],[0,0]]))            # esperado: 3
