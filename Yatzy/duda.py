 @staticmethod
    def one_pair(*dice):
        for dado in range(6):
            if dice.count(dado) >= 2:
                return 2 * dado
        return 0

    @staticmethod
    def three_pair(*dice):
        for dado in range(6):
            if dice.count(dado) >= 3:
                return 3 * dado
        return 0

    @staticmethod
    def four_pair(*dice):
        for dado in range(6):
            if dice.count(dado) >= 4:
                return 4 * dado
        return 0