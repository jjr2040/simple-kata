
class Stats:
    def calc_stats(self, entrada):
        num_elements = self.num_elements(entrada)
        min_elements = self.min_elements(entrada)
        max_elements = self.max_elements(entrada)
        avg_elements = self.avg_elements(entrada)

        resp = [
            num_elements,
            min_elements,
            max_elements,
            avg_elements
        ]

        return resp

    def num_elements(self, string):
        return len(string.split(',')) if string.strip() is not '' else 0

    def min_elements(self, string):
        if string.strip() is '':
            return 0
        else:
            return min(self.string_array_to_int_array(string))

    def max_elements(self, string):
        if string.strip() is '':
            return 0
        else:
            return max(self.string_array_to_int_array(string))

    def avg_elements(self, string):
        if string.strip() is '':
            return 0
        else:
            return 1

    def string_array_to_int_array(self, string):
        return [int(x) for x in string.split(',')]
