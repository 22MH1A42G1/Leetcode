class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) < 2:
            return 0
        s = 0
        b = 0
        be = 0
        for r in bank:
            be = 0
            for c in r:
                if c == '1':
                    be += 1
            s += be * b
            b = be or b
        return s