
class Stats:
    def calc_stats(self, entrada):
        num_elements = self.num_elements(entrada)

        resp = [
            num_elements
        ]

        return resp

    def num_elements(self, string):
        return len(string.split(','))
