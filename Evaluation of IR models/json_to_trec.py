# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
#import urllib.request 
from urllib.request import urlopen
import urllib

from langdetect import detect

models = ['BM25','DFR','LM']
for m in  models:
	count=1
	with open('test_queries.txt',encoding="utf-8") as f:
		for line in f:
			query= line.strip('\n').replace(':','')
			query= query[4:]
			
			try:
				lang = detect(query)
			except:
				lang="text_en"
			if lang=="de":
				ll = "text_de"
			elif lang=="ru":
				ll = "text_ru"
			else:
				ll ="text_en"


			query= urllib.parse.quote(query)
			

			inurl = 'your solr host'+m+'/select?df=' + ll + '&fl=score,id&indent=on&q=' + query + '&rows=20&wt=json'
			outfn = m+'.txt'


	# change query id and IRModel name accordingly
			IRModel='default'
			outf = open(outfn, 'a+')
			data = urlopen(inurl)
	# if you're using python 3, you should use
	# data = urllib.request.urlopen(inurl)
			
			docs = json.load(data)['response']['docs']
	# the ranking should start from 1 and increase
			rank = 1
			
			qid = str(count).zfill(3)
			for doc in docs:

				
				outf.write(qid+' '+'Q0'+' '+ str(doc['id'])+' '+str(rank)+' '+str(doc['score'])+' '+IRModel+'\n' )
				rank+=1
				
			outf.close()
			count+=1
		
