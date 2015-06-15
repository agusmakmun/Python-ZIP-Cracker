
import os, time, sys
import itertools, string
import zipfile

class zipCrack:
    def _checkRoot(self):
        if os.getuid() != 0:
            print "[-] Please Access as root..!"
            sys.exit()
        else:
            pass
  
    def _createWordlist(self, min_length, max_length):
        min_length = min_length
        max_length = max_length
        create = open('wordlist.txt', 'w')
        chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
        print "[+] Create Wordlist file in: { wordlist.txt }"
        print "[+] Please waiting..."
        
        for n in range(min_length, max_length+1):
            for xs in itertools.product(chrs, repeat=n):
                saved = ''.join(xs)
                create.write("%s\n" % saved)
        create.close()
        
    def _getWordlist(self, zipFile, wordList):
        password = None
        zipFile = zipfile.ZipFile(zipFile)
        with open(wordList, 'r') as f:
            for line in f.readlines():
                password = line.strip('\n')
                try:
                    zipFile.extractall(pwd=password)
                    print "[+] Password Found: { %s }" % password
                    print "[+] CTRL + Z, to exit."
                except:
                    pass

    def main(self):
        print """
              +------------------------------------------------------+
              |         { Welcome to Python Zip Cracker }            |
              |  Created By      : Agus Makmun (Summon Agus)         |
              |  Blog            : bloggersmart.net - python.web.id  |
              |  Repository      : github.com/agusmakmun             |
              +------------------------------------------------------+ 
              """
        print "[+] Please choice this options:\n 1. Get Password with Brute Force\n 2. Get Password with Wordlist File."
        inp_usr = raw_input("[+] Enter Options: ")
        mome = zipCrack()
        if inp_usr == '1':
            zipFile = raw_input("[+] Enter *.zip Filename (ex: myzip.zip): ")
            min_length = input("[+] Enter Integer Min-Length (ex: 1): ")
            max_length = input("[+] Enter Integer Max-Length (ex: 2): ")
            wordList = 'wordlist.txt'
            if min_length > max_length:
                print "[-] Upps Failed..!! Min-Length must smaller or as same as Max-Length."
                sys.exit()
            else:
                pass
            mome._createWordlist(min_length, max_length)
            print "[+] Getting Password..."
            time.sleep(1)
            mome._getWordlist(zipFile, wordList)

        elif inp_usr == '2':
            zipFile = raw_input("[+] Enter *.zip Filename (ex: myzip.zip): ")
            wordList = raw_input("[+] Enter Wordlist File (ex: wordlist.txt): ")
            mome._getWordlist(zipFile, wordList)
            
if __name__ == "__main__":
    mome = zipCrack()
    mome._checkRoot()
    mome.main()
