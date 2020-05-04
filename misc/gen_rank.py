# generate ranks for mid2020

def read_csv(fname):
    import csv

    with open(fname, 'r') as f:
        n = []
        s = csv.reader(f, delimiter=',')
        for i, row in enumerate(s):
            if i == 0:
                continue
            n.append(row[0])
        return n

def write_csv(fname, n):
    import csv
    import random

    with open(fname, 'w') as f:
        s = csv.writer(f, delimiter=',')
        s.writerow(['Ogrenci Numarasi', 'Rank'])

        ranks = []
        for n in nums:
            x = random.randint(16**3, (16**4)-1)
            # make sure all of them are unique
            if x not in ranks:
                ranks.append(hex(x))
        # if not, just exit without writing
        if len(nums) != len(ranks):
            raise ValueError
        else:
            for i, n in enumerate(nums):
                s.writerow([n, ranks[i]])


if __name__ == "__main__":
    fname = 'elm234_liste.csv'
    nums = read_csv(fname)
    write_csv('elm234_ranks.csv', nums)