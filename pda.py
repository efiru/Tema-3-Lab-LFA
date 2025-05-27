import random

V = {'S'}
Sigma = {'a', 'b'}
start = 'S'
P = {
    'S': ['aSb', ''],

}

def generate_strings(max_strings=10, max_length=10):
    results = set()
    def expand(symbol):
        if len(symbol) > max_length:
            return
        if all(c in Sigma for c in symbol):
            results.add(symbol)
            return
        i = next(i for i, c in enumerate(symbol) if c in V)
        for prod in P[symbol[i]]:
            expand(symbol[:i] + prod + symbol[i+1:])
    expand(start)
    lst = list(results)
    random.shuffle(lst)
    return lst[:max_strings]

def derive(target):
    path = []
    L = len(target)

    def dfs(current):
        path.append(current)


        if current == target:
            return True


        term_count = sum(1 for c in current if c in Sigma)

        if term_count > L or all(c in Sigma for c in current):
            path.pop()
            return False


        i = next(i for i, c in enumerate(current) if c in V)
        for prod in P[current[i]]:
            next_form = current[:i] + prod + current[i+1:]
            if dfs(next_form):
                return True

        path.pop()
        return False

    dfs(start)
    return path if path and path[-1] == target else []

def recognize(s):
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == 'a'*half and s[half:] == 'b'*half

if __name__ == '__main__':
    print("Siruri generate:", generate_strings())

    target = 'aaabbb'
    derivation = derive(target)
    if derivation:
        print("Derivarea pentru", target, "este:", " -> ".join(derivation))
    else:
        print(f"Nu se poate deriva {target}")

    print("Recunoaste 'aabbb':", recognize('aabbb'))
    print("Recunoaste 'aaabbb':", recognize('aaabbb'))