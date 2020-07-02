# Translator
##

from bs4 import BeautifulSoup


def getTranslation():

    #div class = tlid-result result-dict-wrapper
     #div class = result tlid-copy-target
      #div class = text-wrap tlid-copy-target
       #div class = result-shield-container tlid-copy-target
        #span class = tlid-translation translation
         #<span title class> translation </span>
    
    
    print soup.find('span', id="result_box")


def menu(l):
    
    valid_input = False
    function = 0
    while not valid_input:
        try:
            function = int(raw_input('''What Do You Want To Do?
Press (1) for English to {0}
Press (2) for {0} to English
Press (3) to Exit
'''.format(l)))
            if function > 0 and function < 4:
                return function
            else:
                print 'Enter a number between 1 and 3'
                
        except ValueError:
            print 'Enter a number'
            
    
if __name__ == '__main__':
    finished = False

    soup = ''
    lang = ''

    lang = raw_input('Enter a language:\n')
    f = menu(lang)

    while not finished:
        global soup
        w = raw_input('Enter a word:\n')
        #TODO: find spaces and replace them with '%'
        if f == 1:
            soup = BeautifulSoup(html_doc,
    'https://translate.google.com/#view=home&op=translate&sl={0}&tl={1}&text={2}'.format('en','es', txt))
        elif f == 2:
            soup = BeautifulSoup(html_doc,
    'https://translate.google.com/#view=home&op=translate&sl={0}&tl={1}&text={2}'.format('es','en', txt))
        else:
            finished = True

        getTranslation()
    
