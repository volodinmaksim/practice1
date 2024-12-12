class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            all_line = []
            with open(file_name) as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans(".,=!?;:", "       "))
                    line = line.replace(" - ", " ")
                    line = line.split()
                    all_line += line
            all_words[file_name] = all_line
        return all_words

    def find(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            iterator = 1
            for word_in_file in words:
                if word_in_file == word.lower():
                    find_words[name] = iterator
                    break
                iterator += 1
        return find_words

    def count(self, word):
        count_words = {}
        for name, words in self.get_all_words().items():
            count = 0
            for word_in_file in words:
                if word_in_file == word.lower():
                    count += 1
            count_words[name] = count

        return count_words


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))