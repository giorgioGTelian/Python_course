import glob

# - the glob module finds all the path names matching a spcific pattern
# according to the rules used by the unix shell

#search a specific thing
print(glob.glob(".gitignore"))
#search everything
print(glob.glob("*.*"))

#matches any charatcter in the sequence []:
print(glob.glob("[].py"))

#[!] match any carachter not in a sequence:
print(glob.glob("[!n].py"))



globs = glob.iglob("**/**.py", #what
                root_dir="/users/elian", #where
                recursive= True, #all the time
                include_hidden= True)#include hidden file

for x in globs: #search until you find main.py
  if x == "main.py":
    break
    print(globs.__next__())
