aplhas=['a','b','c']
val_alpha=iter(aplhas)

while True:
    try:
        item=next(val_alpha)
        print(item)
    except StopIteration:
        break

# print(val_vowels)
# print(dir(val_vowels))
# print(next(val_vowels))
# print(next(val_vowels))
# print(next(val_vowels))
# print(next(val_vowels))
print("")

class TestRange:
    def __init__(self, start, end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start>=self.end:
            raise StopIteration
        current=self.start
        self.start+=1
        return current
    
number=TestRange(1,5)

print(next(number))
print(next(number))

for num in number:
    print(num)
print("")

class Sentence:
    def __init__(self, sentence):
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]
    
def sentence(sentence):
    for val in sentence.split():
        yield word

sent=Sentence("Hello this is iterator test")
for word in sent:
    print(word)

print(next(sent))