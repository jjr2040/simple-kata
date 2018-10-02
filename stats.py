
class Stats:
    def calc_stats(self, entrada):
        num_elements = self.num_elements(entrada)
        min_elements = self.min_elements(entrada)
        max_elements = self.max_elements(entrada)

        resp = [
            num_elements,
            min_elements,
            max_elements
        ]

        return resp

    def num_elements(self, string):
        return len(string.split(',')) if string.strip() is not '' else 0

    def min_elements(self, string):
        return int(min(string.split(','))) if string.strip() is not '' else 0

    def max_elements(self, string):
        return int(max(string.split(','))) if string.strip() is not '' else 0
