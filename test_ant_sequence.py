import unittest
from ant_sequence_module import ant_sequence, solution

class TestAntSequence(unittest.TestCase):
    def test_ant_sequence(self):
        self.assertEqual(ant_sequence(1), "1")
        self.assertEqual(ant_sequence(3), "21")
        self.assertEqual(ant_sequence(9), "31131211131221")
        self.assertEqual(ant_sequence(15), "311311222113111231131112132112311321322112111312211312111322212311322113212221")
        
    def test_solution(self):
        self.assertEqual(solution("1"), "1")
        self.assertEqual(solution("21"), "21")
        self.assertEqual(solution("31131211131221"), "11")
        self.assertEqual(solution("311311222113111231131112132112311321322112111312211312111322212311322113212221"), "21")
       
if __name__ == '__main__':
    unittest.main()
