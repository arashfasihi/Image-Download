import urllib
import sys
from threading import Thread

def ProcessURL(url):
      try:
        IMAGE = url.split('/')[-1]
        resource = urllib.urlopen(url)
        output = open(IMAGE,"wb")
        output.write(resource.read())
        output.close()
      except:
        print "Something went wrong trying to download URL : " + url
        print "Check the validity of the URL!"

def ProcessFile(fileName):      
  try:
    input_file = open(fileName,'r')
    importedURLs = input_file.read().split('\n')
  except IOError:
    print "Could not read file!"
  except ValueError:
    print "Check your file for proper format!"
    input_file.close()
  else:
    threads = []
    for line in importedURLs:  
        URL = line
        t = Thread(target=ProcessURL, args=(URL, ))
        t.start()
        threads.append(t)     

    for t in threads:
      t.join()       
    input_file.close()
    print "Downloads completed.."


def main():
  ProcessFile(sys.argv[1])
  

if __name__ == '__main__':
  main()
