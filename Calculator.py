class Calculator:
    result = 0
    intermediate_results = []

    def add(self, a, b):
        add = a + b
        self.intermediate_results.append(add)
        return add

    def subtract(self, a, b):
        subtract = a - b
        self.intermediate_results.append(subtract)
        return subtract

    def divide(self, a, b):
        divide = int(a / b)
        self.intermediate_results.append(divide)
        return divide

    def results(self):
        return self.intermediate_results

    def clear(self):
        self.intermediate_results.clear()
        self.result = 0
