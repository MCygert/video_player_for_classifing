import unittest

from FramesCache import FramesCache


class MyTestCase(unittest.TestCase):

    def test_initalizing(self):
        # given
        test_object = FramesCache(10)
        # when
        test_object.append(5)
        test_object.append(4)
        test_object.append(8)
        test_object.append(2)
        test_object.append(9)
        test_object.append(1)
        # then
        self.assertEqual(test_object.size, 10)
        self.assertEqual(test_object.tail, 1)
        self.assertEqual(test_object.head, 6)
        self.assertEqual(test_object.circled, False)



    def test_circling(self):
        # given
        test_object = FramesCache(4)
        # when
        test_object.append(5)
        test_object.append(4)
        test_object.append(8)
        test_object.append(2)
        test_object.append(9)
        test_object.append(1)
        # then
        self.assertEqual(test_object.size, 4)
        self.assertEqual(test_object.tail, 3)
        self.assertEqual(test_object.head, 2)
        self.assertEqual(test_object.circled, True)


    def test_if_dumping_gives_frames_in_correct_sequence(self):
        # given
        test_object = FramesCache(4)
        test_object.append(5)
        test_object.append(4)
        test_object.append(8)
        test_object.append(2)
        test_object.append(9)
        test_object.append(1)
        # when
        test_results = test_object.dump()
        # then
        self.assertEqual(test_object.size, 4)
        self.assertEqual(test_object.tail, 3)
        self.assertEqual(test_object.head, 2)
        self.assertEqual(test_object.circled, True)
        self.assertEqual(test_results[0], 8)
        self.assertEqual(test_results[1], 2)
        self.assertEqual(test_results[2], 9)
        self.assertEqual(test_results[3], 1)


if __name__ == '__main__':
    unittest.main()
