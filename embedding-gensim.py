# import modules & set up logging
import gensim, os
# print os.listdir('.')
# f=open('/tmp/Oxford_English_Dictionary.txt', 'r')
# contends=f.read()
# f.close()
# lines=contends.split("\n")
#
# sentences=[[]]
# for line in lines:
#     sentences.append(line.split(" "))
# # train word2vec on the two sentences
model = gensim.models.Word2Vec.load('/tmp/mymodel')

print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)