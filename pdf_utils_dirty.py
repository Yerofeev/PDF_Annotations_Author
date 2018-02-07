import popplerqt5,os,shutil
#import inspect
#from itertools import *
dict_results = {}           
annot_users = ['qq','123']   
output_dir = os.path.join('/home/user/Test','test')
#shutil.rmtree(output_dir)
def change_Annotations(fname):
    dict_results[fname]={}
    page_counter = 0
    pdf = popplerqt5.Poppler.Document.load(fname)
    while True:
#print(''.join("\n{0}".format(i) for i in (pdf.page(0).annotations()) if isinstance(i, popplerqt5.Poppler.HighlightAnnotation))) #+++
        try:
            annotations = [i for i in pdf.page(page_counter).annotations() if isinstance(i, popplerqt5.Poppler.HighlightAnnotation)]
            print(page_counter)
            page_counter+=1
            for i in annotations:
                #print('blue:'+str(annot.style().color().blue()))
                print(i.author())
                for annot_user in annot_users:
                    dict_results[fname][annot_user] = 0
                    if i.author() == annot_user:
                        i.setAuthor('It Works!!!!!!!!!!')
                        dict_results[fname][annot_user]+=1
                    if annot.author() in dict_results[fname]:
                        dict_results[fname][annot.author()]+=1
                    else:
                        dict_results[fname][annot.author()]=1                        
        except AttributeError:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)            
            file2 = os.path.join(output_dir,'~'+os.path.basename(filename))
            print(file2)
            c=pdf.pdfConverter()
            c.setOutputFileName(file2)
            c.setPDFOptions(c.WithChanges)
            c.convert()
            print(dict_results)
            return
#filename = '/home/user/Test/test.pdf'
#change_Annotations(filename)
#for root, folder, documents in os.walk(os.path.dirname('/home/user/Test')):
#    for document in documents:
#        if document.endswith(".pdf"):
#            filename = (os.path.join(root, document))
#            change_Annotations(filename)
for document in os.listdir('/home/user/Test'):
    if document.endswith(".pdf"):
        filename = (os.path.join("/home/user/Test", document))
        change_Annotations(filename)   