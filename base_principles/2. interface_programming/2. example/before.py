# Класс компании жестко привязан к конкретным сотрудникам

# Не очень хорошо, т.к код будет усложняться в случае, если будут добавляться
# новые сотрудники и компании


class Designer:
    def design_architecture(self):
        pass


class Programmer:
    def write_code(self):
        pass


class Tester:
    def test_software(self):
        pass


class Company:
    def create_software(self):
        d = Designer()
        d.design_architecture()
        p = Programmer()
        p.write_code()
        t = Tester()
        t.test_software()
