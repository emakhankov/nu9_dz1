import unittest
import unittest.mock
import io


import bag
import barrel
import card
import player


class MyTestCase(unittest.TestCase):

    def test_barrel1(self):

        test_barrel = barrel.Barrel(50)
        self.assertEqual(test_barrel.num, 50)

    def test_barrel2(self):

        test_barrel = barrel.Barrel(25)
        self.assertEqual(test_barrel.get_num(), 25)

    def test_bag(self):

        test_bag = bag.Bag()
        self.assertTrue(isinstance(test_bag.barrels, set))

    def test_bag_len(self):

        test_bag = bag.Bag()
        self.assertEqual(len(test_bag), 90)

    def test_items(self):

        test_bag = bag.Bag()
        bags = set()
        for b in test_bag:
            bags.add(str(b))
        self.assertEqual(len(bags), 90)

    def test_bag_get_barrel(self):

        test_bag = bag.Bag()
        bag_count = test_bag.get_count()
        self.assertEqual(bag_count, 90)

    def test_bag_get_barrel(self):

        test_bag = bag.Bag()
        test_barrel = test_bag.get_barrel()
        self.assertEqual(test_bag.get_count(), 89)
        self.assertFalse(test_barrel in test_bag.barrels)

    def test_bag_90(self):

        test_bag = bag.Bag()
        for _ in range(90):
            test_bag.get_barrel()
        self.assertTrue(test_bag.get_barrel() is None)

    def test_bag_equal(self):

        test_bag = bag.Bag()
        test_bag2 = bag.Bag()
        self.assertEqual(test_bag, test_bag2)
        test_bag.get_barrel()
        self.assertNotEqual(test_bag, test_bag2)
        self.assertNotEqual(test_bag, 0)

    def test_bag_str(self):

        test_bag = bag.Bag()
        self.assertGreater(str(test_bag).find('90'), -1)
        for _ in range(90):
            test_bag.get_barrel()
        self.assertEqual(str(test_bag), 'Пустой бочонок')

    def test_bag_contains(self):

        test_bag = bag.Bag()
        barrel90 = barrel.Barrel(90)
        self.assertIn(barrel90, test_bag)
        some_barrel = test_bag.get_barrel()
        self.assertNotIn(some_barrel, test_bag)

    def test_card(self):

        test_card = card.Card()
        self.assertEqual(len(test_card.lines), 3)
        self.assertEqual(len(test_card.lines[0]), 9)
        self.assertEqual(len(test_card.gaps), 3)
        self.assertEqual(len(test_card.nums), 3)

    def test_card_amount_num(self):

        test_card = card.Card()
        self.assertEqual(test_card.amount_num(), 15)

    def test_card_can_accept_barrel(self):

        test_card = card.Card()
        test_barrels = []
        for line in range(3):
            for pos in test_card.lines[line]:
                if isinstance(pos, int):
                    ans = test_card.can_accept_barrel(int(pos))
                    self.assertTrue(ans)
                    test_barrels.append(int(pos))

        for i in range(1, 91):
            if not (i in test_barrels):
                ans = test_card.can_accept_barrel(i)
                self.assertFalse(ans)

    def test_card_accept_barrel(self):

        test_card = card.Card()
        test_barrels = []
        for line in range(3):
            for pos in test_card.lines[line]:
                if isinstance(pos, int):
                    ans = test_card.accept_barrel(int(pos))
                    self.assertTrue(ans)
                    test_barrels.append(int(pos))

        for i in range(1, 91):
            if not (i in test_barrels):
                ans = test_card.accept_barrel(i)
                self.assertFalse(ans)

        self.assertEqual(test_card.amount_num(), 0)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_card_print_card(self, mock_stdout):

        test_card = card.Card()
        test_card.print_card()
        test_text = mock_stdout.getvalue().lower()
        for pos in test_card.lines[1]:
            if isinstance(pos, int):
                self.assertGreater(test_text.find(str(pos)), -1)

    def test_player_init(self):

        test_player = player.Player('www')
        self.assertEqual(test_player.name, 'www')
        self.assertIsInstance(test_player.card, card.Card)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_print_card(self, mock_stdout):

        test_player = player.Player('www')
        test_player.print_card()
        test_text = mock_stdout.getvalue().lower()
        for pos in test_player.card.lines[1]:
            if isinstance(pos, int):
                self.assertGreater(test_text.find(str(pos)), -1)
        self.assertRegex(test_text, r'карточка игрока')

    def test_player_ask_for_barrel_and_winner(self):

        test_player = player.Player('www')
        i = 0
        for line in range(3):
            for pos in test_player.card.lines[line]:
                i += 1
                if i < 5:
                    self.assertFalse(test_player.is_winner())
                if isinstance(pos, int):
                    test_player.ask_for_barrel(barrel.Barrel(int(pos)))

        self.assertEqual(test_player.card.amount_num(), 0)
        self.assertTrue(test_player.is_winner())
        test_player.ask_for_barrel(barrel.Barrel(10))

    def test_human_player_init(self):

        test_player = player.HumanPlayer('www')
        self.assertEqual(test_player.name, 'Человек www')
        self.assertIsInstance(test_player.card, card.Card)

    def test_human_player_ask_for_barrel_and_winner(self):

        def delegate(player):

            return True

        def delegate2(player):

            return False

        test_player = player.HumanPlayer('www')
        i = 0

        for line in range(3):
            for pos in range(1,91):
                i += 1
                if i < 5:
                    self.assertFalse(test_player.is_winner())
                test_player.ask_for_barrel(barrel.Barrel(pos), delegate)

        self.assertEqual(test_player.card.amount_num(), 0)
        self.assertTrue(test_player.is_winner())

        test_player = player.HumanPlayer('www')
        i = 0
        for line in range(3):
            for pos in test_player.card.lines[line]:
                i += 1
                if i < 5:
                    self.assertFalse(test_player.is_winner())
                if isinstance(pos, int):
                    test_player.ask_for_barrel(barrel.Barrel(int(pos)), None)

        self.assertEqual(test_player.card.amount_num(), 0)
        self.assertTrue(test_player.is_winner())

        test_player = player.HumanPlayer('www')
        i = 0
        for line in range(3):
            for pos in range(1, 91):
                i += 1
                if i < 5:
                    self.assertFalse(test_player.is_winner())
                test_player.ask_for_barrel(barrel.Barrel(pos), delegate2)

        self.assertEqual(test_player.card.amount_num(), 15)
        self.assertFalse(test_player.is_winner())

    def test_computer_player_init(self):

        test_player = player.ComputerPlayer('www')
        self.assertEqual(test_player.name, 'Компьютер www')
        self.assertIsInstance(test_player.card, card.Card)

    def test_computer_player_ask_for_barrel_and_winner(self):

        test_player = player.ComputerPlayer('www')
        i = 0
        for line in range(3):
            for pos in test_player.card.lines[line]:
                i += 1
                if i < 5:
                    self.assertFalse(test_player.is_winner())
                if isinstance(pos, int):
                    test_player.ask_for_barrel(barrel.Barrel(int(pos)), None)

        self.assertEqual(test_player.card.amount_num(), 0)
        self.assertTrue(test_player.is_winner())


if __name__ == '__main__':
    unittest.main()
