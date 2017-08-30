 import collections, re
 texts = ['John likes to watch movies. Mary likes too.',
   'John also likes to watch football games.']
 bagsofwords = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in texts]
 bagsofwords[0]
Counter({'likes': 2, 'watch': 1, 'Mary': 1, 'movies': 1, 'John': 1, 'to': 1, 'too': 1})
 bagsofwords[1]
Counter({'watch': 1, 'games': 1, 'to': 1, 'likes': 1, 'also': 1, 'John': 1, 'football': 1})
 sumbags = sum(bagsofwords, collections.Counter())
 sumbags
Counter({'likes': 3, 'watch': 2, 'John': 2, 'to': 2, 'games': 1, 'football': 1, 'Mary': 1, 'movies': 1, 'also': 1, 'too': 1})
 