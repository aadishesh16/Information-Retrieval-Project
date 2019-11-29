from collections import defaultdict
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("path1")
parser.add_argument("path2")
parser.add_argument("path3")
args = parser.parse_args()
index= defaultdict(list) 

count_w= defaultdict(list)
with open(args.path1,"r") as f:
    for line in f:
        f_r = line.split()
        doc_id = int(f_r[0]) 
        f_r = f_r[1:]
        for i,j in enumerate(f_r) :
            count_w[doc_id] = i+1
        f_r = set(f_r)
        for w in f_r :
            if w not in index:
                index[w]= []
                index[w].append(doc_id)
            else:
                index[w].append(doc_id)
index = dict(index)
total_docs=0
index1= defaultdict(list) 

with open(args.path1,"r") as fa:
    for lines in fa:
        total_docs =total_docs+1
        f_sr= lines.split()
        doc_ids = int(f_sr[0])
        f_sr=f_sr[1:]
        abc = " ".join(f_sr)
        index1[doc_ids] = abc



def counter(x):
    sss=set(x)
    return ([(i,x.count(i)) for i in sss])


def tf_idf(lists,keylist):
	tfidf_final = {}
	for i in lists:
		tf_idf_final=0
		for k in keylist:
			extracted_data =[]
			co =0
			extracted_data.append(index1[i].split())
			if(any(k in s for s in extracted_data)):
				co +=1
			tf = co/count_w[i]
			idf =total_docs/len(index[k]) 
			tf_idff = tf*idf
			tf_idf_final = tf_idf_final+tf_idff
		tfidf_final[i]=tf_idf_final
	sorted_tf = sorted(tfidf_final.items(), key=lambda tftf: tftf[1],reverse=True)
	return sorted_tf
with open(args.path3,"r") as g, open(args.path2,"w") as h:
	for line in g:
		ab= line.split()
		print("GetPostings",*ab)

		print("DaatAnd",*ab)
		print("TF-IDF",*ab)
		print("DaatOr",*ab)
		print("TF-IDF",*ab)
		re = ab[0]
		ree = ab[1]
		fref = index[re]
		xref = index[re]
		unionlist=[]
		count =0
		finu=set()
		uvi =0
		for i in ab:
			umid=[]

			h.write("GetPostings \n")
			h.write(str(i)+"\n")
			for  uv in index[i]:
				finu.add(uv)
				count+=1
			for xx in index[i]:
				umid.append(xx)

			u,v=0,0
			m = len(xref)
			n = len(umid)
			uvi = m*n			
			while u<m and v<n:
				if xref[u]<umid[v]:
					unionlist.append(xref[u])
					u+=1
				elif umid[v]<xref[u]:
					unionlist.append(umid[v])
					v+=1
				else:
					unionlist.append(umid[v])
					u+=1
					v+=1
			while u<m:
				unionlist.append(xref[u])
				u+=1
			while v<n:
				unionlist.append(umid[v])
				v+=1



			index[i] = str(index[i]).strip("[]")
			index[i] = index[i].replace(",","")

			h.write("Postings list: "+(str(index[i]).replace("'",""))+"\n")

			fref = [u for u in fref if u in umid ]

    	

		ff= len(finu)
		l = len(fref)
		uniontf = tf_idf(finu,ab)
		uniontf=dict(uniontf)
		uniontf=uniontf.keys()		
		uniontf= str(uniontf).replace("dict_keys","")
		uniontf= str(uniontf).strip("()")
		uniontf= str(uniontf).strip("[]")
		uniontf= str(uniontf).replace(",","")
		intertf = tf_idf(fref,ab)
		intertf=dict(intertf)
		intertf=intertf.keys()		
		intertf= str(intertf).replace("dict_keys","")
		intertf= str(intertf).strip("()")
		intertf= str(intertf).strip("[]")
		intertf= str(intertf).replace(",","")		
		h.write("DaatAnd \n")
		ab= str(ab).strip("[]")
		ab=ab.replace("'","")
		ab=ab.replace(",","")
		finu = str(finu).strip("{}")
		finu = finu.replace(",","")
		h.write(str(ab)+"\n")
		if not fref:
			h.write("Results: empty\n")
		else :
			fref= str(fref).strip("[]")
			fref = fref.replace(",","")
			h.write("Results: "+str(fref)+"\n")
		h.write("Number of documents in results: "+str(l)+"\n")
		h.write("Number of comparisons: "+str(uvi)+"\n")
		h.write("TF-IDF \n")
		if not intertf:
			h.write("Results: "+str("empty")+"\n")
		else:
			h.write("Results: "+str(intertf)+"\n")
		h.write("DaatOr \n")
		h.write(str(ab)+"\n")
		h.write("Results: "+str(finu)+"\n")
		h.write("Number of documents in results: "+str(ff)+"\n")
		h.write("Number of comparisons: "+str(count)+"\n")
		h.write("TF-IDF \n")
		h.write("Results: "+str(uniontf)+"\n" )
		h.write("\n")				
