
class insertion_sort():
    def __init__(self):
        """
        This class is to perform Insertion Sort on a given List/Array
        """
        self.verified = False
        self.getSorted = []

    def _verify_array(self, list_to_sort):
        """
        This method is used for verifing either array contain invalid entries.
        """
        try:
            for element in list_to_sort:
                int(element)
        except:
            exit('Please input a valid numerical values')

    def sort(self, list_to_sort):
        """ This method is used to sort the given array
                """
        # Verify
        if self.verified is False:
            self._verify_array(list_to_sort)
            self.verified = True

        # Logic
        for element in range(1, len(list_to_sort)):
            pointer = list_to_sort[element]
            before_pointer = element-1

            while before_pointer >= 0 and pointer < list_to_sort[before_pointer]:
                list_to_sort[before_pointer+1] = list_to_sort[before_pointer]
                before_pointer -= 1

            list_to_sort[before_pointer+1] = pointer

        self.getSorted = list_to_sort
