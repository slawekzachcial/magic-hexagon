# Magic Hexagon

[main.py](main.py) is a Python implementation to solve [Magic Hexagon](https://en.wikipedia.org/wiki/Magic_hexagon).

The approach I used is as follows.

Given a hexagon (example: order=3, numbers=1..19, M=38) with cells indexed as
below (iN is a cell index),

```
      i0    i1    i2
   i11   i12   i13   i3
i10   i17   i19   i14   i4
   i9    i16   i15   i5
      i8    i7    i6
```

find all combinations of numbers that correspond to the outer ring (cells i0..i11)
so that the sums of numbers of the sides are equal to M (example for M=38:
sum(i0..i2)==38, sum(i2..i4)==38, sum(i4..i6)==38, sum(i6..i8)==38,
sum(i8..i10)==38, sum(i10..i0)==38).

Then for each ring find all combinations of inner rings (cells i12..i17)
such that the sum of each side is equal to M minus the numbers from the outer
ring located at the same line (example for i12..i13: M - v[i11] - v[i3]).

Continue the process recursively finding all combinations of deeper inner rings
until reaching the central cell (example: i19) which represents the last number.

Below is the output for order=3, numbers=1..19, M=38:

```
$ ./main.py
[3, 17, 18, 19, 7, 1, 11, 16, 2, 5, 6, 9, 12, 4, 8, 14, 10, 13, 15]
[3, 19, 16, 17, 7, 2, 12, 18, 1, 5, 4, 10, 11, 6, 8, 13, 9, 14, 15]
[9, 11, 18, 14, 6, 1, 17, 15, 8, 5, 7, 3, 13, 4, 2, 19, 10, 12, 16]
[9, 14, 15, 11, 6, 8, 13, 18, 1, 5, 4, 10, 17, 7, 2, 12, 3, 19, 16]
[10, 12, 16, 13, 4, 2, 19, 15, 8, 5, 7, 3, 14, 6, 1, 17, 9, 11, 18]
[10, 13, 15, 12, 4, 8, 14, 16, 2, 5, 6, 9, 19, 7, 1, 11, 3, 17, 18]
[15, 13, 10, 14, 8, 4, 12, 9, 6, 5, 2, 16, 11, 1, 7, 19, 18, 17, 3]
[15, 14, 9, 13, 8, 6, 11, 10, 4, 5, 1, 18, 12, 2, 7, 17, 16, 19, 3]
[16, 12, 10, 19, 2, 4, 13, 3, 7, 5, 8, 15, 17, 1, 6, 14, 18, 11, 9]
[16, 19, 3, 12, 2, 7, 17, 10, 4, 5, 1, 18, 13, 8, 6, 11, 15, 14, 9]
[18, 11, 9, 17, 1, 6, 14, 3, 7, 5, 8, 15, 19, 2, 4, 13, 16, 12, 10]
[18, 17, 3, 11, 1, 7, 19, 9, 6, 5, 2, 16, 14, 8, 4, 12, 15, 13, 10]
```

The output above presents each result using __linear__ indices insead of
__circular__ ones used in the explanation above. Therefore the first result is:

```
    3   17  18
  19  7   1   11
16  2   5   6   9
  12  4   8   14
    10  13  15
```

## Remaining Implementation Problems

* I could not figure out how to TDD the recursive functions `collectRings` and
  `collectResults`. I had to write these functions first to even imagine how
  they could work. If a function is not testable that's usually a sign of bad
  design?
* I could not figure out how to map __circular__ indexes (better suited in my
  implementation) to __linear__ ones (better suited for result presentation)
  in `ringIndicesToLinear` function.
* I could not figure out how to refactor the functions (especially `collectRings` 
  and `collectResults` to leverage Python `multiprocessing` module's `Pool` -
  in its simplest form it requires a function that can map an input value to a
  result and it can parallelize based on input values collection (see
  [example](https://docs.python.org/3/library/multiprocessing.html#introduction)).
* 3 hours of calculations where not enough to find solutions for order=4
  (`./main.py 4 111 3 39`). Being able to parallelize would certainly be helpful.
