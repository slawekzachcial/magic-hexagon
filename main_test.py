#!/usr/bin/env python3

import unittest
from main import *

class MainTests(unittest.TestCase):
    def test_isRingBaseCompatible_first(self):
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [1, 3, 2]))
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [3, 1, 2]))
        self.assertTrue(isRingBaseCompatible([1, 2, 3], [4, 5, 1]))

    def test_isRingBaseCompatible_last(self):
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [4, 3, 2]))
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [4, 5, 6, 3]))
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [4, 3, 6, 5]))
        self.assertTrue(isRingBaseCompatible([1, 2, 3], [3, 4, 6, 5]))

    def test_isRingBaseCompatible_middle(self):
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [2, 4, 5, 6]))
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [4, 5, 6, 2]))
        self.assertFalse(isRingBaseCompatible([1, 2, 3], [4, 5, 2, 6]))
        self.assertTrue(isRingBaseCompatible([1, 2, 3], [4, 5, 6]))

    def test_isClosingRing(self):
        self.assertTrue(isClosingRing([[1,2],[2,1]]))
        self.assertTrue(isClosingRing([[1,2],[3,4],[2,1]]))
        self.assertFalse(isClosingRing([[1,2],[2,3],[3,2]]))
        self.assertFalse(isClosingRing([[1,2],[2,1],[3,2]]))

    def test_isNextCandidate(self):
        self.assertTrue(isNextCandidate([1, 2], 5, [2, 3]))
        self.assertFalse(isNextCandidate([1, 2], 4, [2, 3]))
        self.assertTrue(isNextCandidate([1, 2, 3], 6, [3, 2, 1]))
        self.assertFalse(isNextCandidate([1, 2], 2, [1, 3]))
        self.assertFalse(isNextCandidate([1, 2], 1, [3, 2]))

    def todo_collectRings(self):
        # TODO: how to test a recursive function
        pass

    def test_rings_notFound(self):
        self.assertEqual(rings([3, 3, 3], [[1,2],[2,3]]), [])

    def test_rings_found(self):
        self.assertEqual(rings([3, 5, 7, 9, 11, 7],
                                    [[1,2],[2,3],[2,1],[3,1],[4,5],[3,4],[5,6],[6,1]]),
                         [[[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]]])

    def test_innerRingSums(self):
        self.assertEqual(innerRingSums([38,38,38,38,38,38],[[1,2,3],[3,4,5],[5,6,7],[7,8,9],[9,10,11],[11,12,1]]),
                          [38-12-4, 38-2-6, 38-4-8, 38-6-10, 38-8-12, 38-2-10])
        self.assertEqual(innerRingSums([100,101,102,103,104,105],[[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13],[13,14,15,16],[16,17,18,1]]),
                         [100-18-5,101-3-8,102-6-11,103-9-14,104-12-17,105-15-2])

    def test_ringToList(self):
        self.assertEqual(ringToList([[1, 2, 3], [3, 4, 5], [5, 6, 1]]),
                         [1, 2, 3, 4, 5, 6])
        self.assertEqual(ringToList([[1,2],[2,3],[3,1]]),
                         [1,2,3])

    def test_sideSize(self):
        self.assertEqual(sideSize(1), 1)
        self.assertEqual(sideSize(7), 2)
        self.assertEqual(sideSize(19), 3)
        self.assertEqual(sideSize(37), 4)
        self.assertRaises(ValueError, sideSize, 5)

    def test_ringIndicesToLinear(self):
        self.assertEqual(ringIndicesToLinear([7]), [7])
        self.assertEqual(ringIndicesToLinear([1, 2, 3, 4, 5, 6, 7]),
                         [1, 2, 6, 7, 3, 5, 4])
        self.assertEqual(ringIndicesToLinear([1,2,3,7,12,16,19,18,17,13,8,4,5,6,11,15,14,9,10]),
                         [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
        self.assertRaises(ValueError, ringIndicesToLinear, [1, 2])

if __name__ == '__main__':
    unittest.main()
