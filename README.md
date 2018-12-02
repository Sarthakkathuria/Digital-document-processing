# Digital-document-processing
In the last years, the spread of computers and the Internet caused a 
significant amount of documents to be available in digital format. 
Collecting them in digital repositories raised problems that go beyond 
simple acquisition issues, and cause the need to organize and classify 
them in order to improve the effectiveness and efficiency of the 
retrieval procedure. The success of such a process is tightly related to
 the ability of understanding the semantics of the document components 
and content. Since the obvious solution of manually creating and 
maintaining an updated index is clearly infeasible, due to the huge 
amount of data under consideration, there is a strong interest in 
methods that can provide solutions for automatically acquiring such a 
knowledge.
# Requirements
sudo apt-get install python-imaging

sudo apt-get install tesseract-ocr
sudo apt-get install python-opencv

# Example

1. First process the image

python process_image.py test.jpg text.jpg



2.Extract text

python extract_text.py


Output:


4 WkiJre €99 Bread

A good, basic white bread.

with

I. 21/2 cups lukewarm water
2 packages dry yeast
1/4 cup honey
1 cup dry mile
2 eggs, beaten
4 cups unbleached white ﬂour

II. 4 teaspoons salt
1/3 cup butter or margarine
3 caps or inore unbleached white ﬂour for forming the dough
1 cup (approx.) white ﬂour for kneadian

Proceed with the directions for recipe #1, adding the beaten eggs afte
stirring in the dry milk.


