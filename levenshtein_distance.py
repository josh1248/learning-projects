sub_cost, ins_cost, del_cost = 1, 0.5, 0.5
#elegant but inefficient as same substrings are considered multiple times
def r_levenshtein(s1, s2):
    runs = [0] #to avoid need for nonlocal declaration in helper
    substrings = set()
    def helper(a, b):
        runs[0] += 1
        substrings.add(a)
        if not a: return len(b)
        elif not b: return len(a)
        else: return min(helper(a[1:], b[1:]) + sub_cost * (a[0] != b[0]),
                         helper(a, b[1:]) + ins_cost,
                         helper(a[1:], b) + del_cost)
    distance = helper(s1, s2)
    print(f"Levenshtein distance: {distance}")
    print(f"Function runs: {runs[0]:,}")
    print(f"Unique substrings considered: {len(substrings)}")

#also gives the edit path to obtain s2 from s1
def constructive_r_levenshtein(s1, s2):
    pass

#DP Hirschberg's algorithm implementation that is more efficient in O(mn) time and O(min{m, n}) space

#r_levenshtein("integrate","differentiate")