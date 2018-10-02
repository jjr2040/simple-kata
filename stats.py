
class Stats:
    def calc_stats(self, entrada):
        num_elements = self.num_elements(entrada)

        if num_elements == 0 or num_elements == 1:
            min_elements = self.min_elements(entrada)
            resp = [
                num_elements,
                min_elements
            ]
        else:

            resp = [
                num_elements
            ]

        return resp

    def num_elements(self, string):
        return len(string.split(',')) if string.strip() is not '' else 0

    def min_elements(self, string):
        return 1 if string.strip() is not '' else 0
