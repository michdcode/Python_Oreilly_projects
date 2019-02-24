import time

my_words = [elt.strip() for elt in open("sonnet_words.txt", "r").readlines()]
# for element in textfile/list
word_list = [elt.strip() for elt in open("sowpods.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in word_list) #set default value to 1
word_set = set(word_list) #remember it's a dictionary without keys, same run time

counter = 0

start = time.time()

for word in my_words:
    if word not in word_set:
        print(word)
        counter += 1

stop = time.time()

print("Total new words: %d" % counter)
print("Total time elapsed: %.1f seconds" % (stop - start))