import unittest


class LiteralValidation(unittest.TestCase):

    def setUp(self):
        self.test_case_correct = '''{name}, ваша запись изменена:
                            ⌚️ {day_month} в {start_time}
                            👩 {master}
                            Услуги:
                            {services}
                            управление записью {record_link}'''

        self.check_list = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']



    def test_text_validation(self):
        # Parsing parametrs from text
        check_lst = frozenset(['{name}', '{day_month}', '{day_of_week}', '{start_time}', '{end_time}', '{master}', '{services}'])
        list_of_parameters_in_text = [x for x in set(
            self.test_case_correct.split()) if x.startswith('{')]

        # Cheaking format of parameters

        for i in list_of_parameters_in_text:
            if i.endswith(','):
                list_of_parameters_in_text.remove(i)
                list_of_parameters_in_text.append(i.removesuffix(','))

        # Test of open/close brackets
        for i in list_of_parameters_in_text:
            self.assertTrue(i.startswith('{') and i.endswith('}'))

        # Test of names of parameters
        for i in list_of_parameters_in_text:
            self.assertTrue(str(i))                
