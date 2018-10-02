
class Stats:
    def calc_stats(self, entrada):
        num_elements = self.num_elements(entrada)

        if num_elements != 0:
            resp = [
                num_elements
            ]
        else:
            min_elements = self.min_elements(entrada)
            resp = [
                num_elements,
                min_elements
            ]

        return resp

    def num_elements(self, string):
        return len(string.split(',')) if string.strip() is not '' else 0

    def min_elements(self, string):
        return 0
