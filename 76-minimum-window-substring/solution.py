from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # quantos de cada char precisamos encontrar
        need = Counter(t)

        # quantos chars distintos de t ainda faltam cobrir
        required = len(need)

        left = 0
        formed = 0  # quantos chars distintos já estão na janela com freq suficiente

        # freq dos chars dentro da janela atual
        window = {}

        # (tamanho, left, right) da melhor janela encontrada
        best = float("inf"), 0, 0

        for right, char in enumerate(s):
            # expande janela adicionando char da direita
            window[char] = window.get(char, 0) + 1

            # verifica se esse char atingiu a freq necessária
            if char in need and window[char] == need[char]:
                formed += 1

            # janela válida: tem todos os chars de t com freq suficiente
            # tenta encolher pela esquerda
            while formed == required and left <= right:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)

                # remove char da esquerda
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if best[0] == float("inf") else s[best[1]: best[2] + 1]


# --- testes ---
print(Solution().minWindow("ADOBECODEBANC", "ABC"))  # esperado: "BANC"
print(Solution().minWindow("a", "a"))                # esperado: "a"
print(Solution().minWindow("a", "aa"))               # esperado: ""
