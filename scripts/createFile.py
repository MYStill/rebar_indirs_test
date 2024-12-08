import os
srcPath="../src/test/"
def createDir(dirName, path):
  os.mkdir(os.path.join(path, dirName))
def createFile(fileName, path):
  with open(os.path.join(path, fileName + ".erl"), 'w') as f:
    f.write("-module(" + fileName + ")." + """
-export([aa/0,bb/0]).
aa() -> a.
bb() -> b.""")
  
for i in ["a","b","c","d"]:
  createDir(i, srcPath)
  createFile(i, srcPath)
  for j in ["a","b","c","d"]:
    inPath=i
    fileName=i+j
    createDir(j, srcPath + inPath)
    createFile(fileName, srcPath + inPath)
    for k in ["a","b","c","d","e","f","g","h","i"]:
      inPath=i + "/" + j
      fileName=i+j + k
      createDir(k, srcPath + inPath)
      createFile(fileName, srcPath + inPath)
      for l in ["a","b","c","d","e","f"]:
        inPath=i + "/" + j + "/" + k
        fileName=i+j + k + l
        createDir(l, srcPath + inPath)
        ##createFile(fileName, srcPath + inPath)
        for m in ["a","b","c","d"]:
          inPath=i + "/" + j + "/" + k + "/" + l
          fileName=i+j + k + l + m
          createDir(m, srcPath + inPath)
          ##createFile(fileName, srcPath + inPath)
          for n in ["a","b","c","d"]:
            inPath=i + "/" + j + "/" + k + "/" + l + "/" + m
            fileName=i+j + k + l + m + n
            createFile(fileName, srcPath + inPath)