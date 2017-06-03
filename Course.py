PAGE = 'https://cobalt.qas.im/api/1.0/courses/filter?q=code:%22'
KEY = 'TVwEIjRZP80vhnY8HhM0OzZCMfydh4lA'


class Course:
    """
    Private Attributes:
    ==================
        @param str code:
            Code for the course
    """
    def __init__(self, code):
        self._course_code = code
        self._mark = 0.0
        self._type = 'Planned'

        try:
            if code[6] == 'Y':
                self.weight = 1.0
            else:
                self.weight = 0.5
        except IndexError:
            self.weight = 0.0

        self.course_count = 1  # Used for abstract courses

        self._is_passed = False

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, new_mark):
        if isinstance(new_mark, float) or isinstance(new_mark, int):
            self._mark = new_mark
        else:
            print('Not a valid mark!')

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        if isinstance(new_type, str) and (new_type == 'Planned' or new_type == 'Taken' or new_type == 'Dropped'):
            self._type = new_type
        else:
            print('Invalid course type!')

    @property
    def course_code(self):
        return self._course_code

    def _update_passed(self):
        """
        Return if the the course passes or not

        :return: bool
        """

        if self.mark >= 50 and (self.type == 'Passed' or self.type == 'Planned'):
            self._is_passed = True
        else:
            self._is_passed = False

    def is_passed(self):
        return self._is_passed

    def __repr__(self):
        return 'Course(' + self.course_code + ')'
