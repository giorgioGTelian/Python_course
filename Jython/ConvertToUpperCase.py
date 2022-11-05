import sys
from java.io import FileOutputStream

class UppercaseFileOutputStream(FileOutputStream):
    def write_upper(self, text):
        text = text.upper()
        self.write(text)

def test(outfilename):
    fos = UppercaseFileOutputStream(outfilename)
    for idx in range(10):
        fos.write_upper('This is line # %d\n' % idx)
    fos.close()
    infile = open(outfilename, 'r')
    for line in infile:
        line = line.rstrip()
        print 'Line: %s' % line

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: extend_fileoutputstream.py <infilename>'
        sys.exit(1)
    test(args[0])

if __name__ == '__main__':
    main()
