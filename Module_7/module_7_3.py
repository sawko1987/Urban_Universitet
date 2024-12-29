class WordsFinder:
    file_names =()
    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for document in self.file_names:
            with open(document, encoding="utf-8") as file:
                line_read = file.read().lower()
                for punctuation in (',', '.', '=', '!', '?', ';', ':', ' - '):
                    if punctuation in line_read:
                        punctuation_line = line_read.replace(punctuation,"")
                line_split = punctuation_line.split()
                all_words[document]= line_split
        return all_words

    def find(self, word):
        self.word = word
        dict_find={}
        number = 0
        for k, v in (self.get_all_words()).items():
            for value in v:
                if value == self.word.lower():
                    number+=1
                    dict_find[k]= number
                    break
                else:
                    number+=1
        return dict_find

    def count(self, word):
        self.word= word
        dict_count = {}
        len_value = 0
        for k,v in (self.get_all_words()).items():
            for value in v:
                if value == self.word.lower():
                    len_value +=1
                dict_count[k] = len_value

        return dict_count






finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

