import os
import pprint
import popplerqt5


def change_annotations(fname, dict_annot, dict_results, origin_dir):
    """Change author of PDF's annotations"""  
    output_dir = os.path.join(origin_dir, 'PDF')
    a_types = (popplerqt5.Poppler.HighlightAnnotation, popplerqt5.Poppler.LineAnnotation,
               popplerqt5.Poppler.GeomAnnotation, popplerqt5.Poppler.InkAnnotation)
    dict_results[fname] = {}
    page_counter = 0
    pdf = popplerqt5.Poppler.Document.load(fname)
    while True:
        try:
            # choose certain types of Annotations
            annotations = [i for i in pdf.page(page_counter).annotations() if (isinstance(i, a_types))]
            page_counter += 1
            if not annotations:
                continue
            for annot in annotations:
                if annot.author() in dict_annot:
                    if annot.author() not in dict_results[fname]:
                        dict_results[fname][annot.author()] = 0                         
                    dict_results[fname][annot.author()] += 1                          
                    annot.setAuthor(dict_annot[annot.author()])             
        except AttributeError:                      # end of the document                     
            break
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        file2 = os.path.join(output_dir, os.path.basename(fname))
        c = pdf.pdfConverter()
        c.setOutputFileName(file2)
        c.setPDFOptions(c.WithChanges)
        c.convert()
    except:
        print('During saving {} error occured'.format(file2))

def main():
    while True:
        dict_results = {}
        dict_annot = {}            
        origin_dir = input('Specify folder with pdf(s): ')
        if not os.path.exists(origin_dir):
            print('Incorrect path') 
        else:
            break
    while True:
        a = input('Enter the Author of Annotation you want to change: ')
        b = input('Change it to: ')
        # put in dictionary the author you want to change: for instance 'i' -> 'Important'
        dict_annot[a] = b
        quest = input('More to change? (y,n): ')
        if quest in {'n', 'N'}:
            break
        else:
            pass
    for document in os.listdir(origin_dir):
        if document.lower().endswith(".pdf"):
            filename = (os.path.join(origin_dir, document))
            change_annotations(filename, dict_annot, dict_results, origin_dir)
    pprint.pprint(dict_results, width=1)
    print('Replacements: ' + str(sum(x for counter in dict_results.values() for x in counter.values())))
    print('Modified PDFs were put in {}/PDF folder'.format(origin_dir))
    
    
if __name__ == '__main__':
    main()
