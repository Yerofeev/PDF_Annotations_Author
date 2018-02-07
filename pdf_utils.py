import popplerqt5,os,pprint
dict_results = {}           
#annot_users = ['qq','qqq','qqqq','`']
#annot_desired = ['ff','fff','ffff','?']
origin_dir =  '/home/user/Test'# '/media/user/Science/EP/3 Enlightened & wondrous world'#  #
output_dir = os.path.join(origin_dir,'test')#'/media/user/Science/NEW 3 Enlightened & wondrous world'#
annotations_types = (popplerqt5.Poppler.HighlightAnnotation, popplerqt5.Poppler.LineAnnotation, popplerqt5.Poppler.GeomAnnotation, popplerqt5.Poppler.InkAnnotation) 
#annotations_types = ({0}.HighlightAnnotation, {0}.LineAnnotation, {0}.GeomAnnotation, {0}.InkAnnotation).format('popplerqt5.Poppler')

def position_to_set_author(author,counter):
    if 'qqqq' in author:
        mult = 4
    elif 'qqq' in author:
        mult = 3
    else:
        mult = 2
    return author[:counter] + 'f'*mult + author[counter+mult:]  

def change_Annotations(fname):
    dict_results[fname]={}
    page_counter = 0
    print(fname)
    pdf = popplerqt5.Poppler.Document.load(fname)
    while True:
        try:
            annotations = [i for i in pdf.page(page_counter).annotations() if (isinstance(i, annotations_types))]
            page_counter+=1

            for annot in annotations:
 #               for annot_user in annot_users:
                       
                if 'qq' in annot.author():
                    if 'uot' not in annot.author():
                        if annot.author() not in dict_results[fname]:
                            dict_results[fname][annot.author()] = 0                         
                        dict_results[fname][annot.author()] += 1                          
                        annot.setAuthor(position_to_set_author(annot.author(),annot.author().find('qq')))
             
        except AttributeError:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            try:
                file2 = os.path.join(output_dir,os.path.basename(filename))
                c=pdf.pdfConverter()
                c.setOutputFileName(file2)
                c.setPDFOptions(c.WithChanges)
                c.convert()
            except Exception:
                return
            return
        
for document in os.listdir(origin_dir):
    if document.lower().endswith(".pdf"):
        filename = (os.path.join(origin_dir, document))
        change_Annotations(filename)   
pprint.pprint(dict_results,width=1)        
print('Replacements: ' + str(sum(x for counter in dict_results.values() for x in counter.values())))