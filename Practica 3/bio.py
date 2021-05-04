from Bio import SeqIO

sequences = SeqIO.parse("P21333.fasta", "fasta")

for record in sequences:
  data1 = str(record.seq.upper()) # the fasta file just have one sequence
  sequences = SeqIO.parse("Q8BTM8.fasta", "fasta")
  for record in sequences:
    data2 = str(record.seq.upper()) # the fasta file just have one sequence
print(data1)
print(data2)

import matplotlib.pyplot as plt

def identity(win_1, win_2, threshold):
    res = len(set(win_1) & set(win_2)) / max(len(win_1), len(win_2)) *100
    # print(res)
    if res >= threshold:
        return True
    else:
        return False

# print(identity(data1,data2,0.4))
def dot_matrix(d1,d2,window,threshold):
  subseq1 = [str(data1)[i: i + window] for i in range(0, len(str(data1)), window)]
  subseq2= [str(data2)[i: i + window] for i in range(0, len(str(data2)), window)]
  # print(len(subseq1))
  # print(len(subseq2))
  # print(identity(subseq1,subseq2,50))
  x=[]
  y=[]
  for  i in range(len(subseq1)):
    for j in range(len(subseq2)):
      if(identity(subseq1[i],subseq2[j],70)):
        x.extend([n for n in range(i*window, (i*window)+window)])
        y.extend([n for n in range(j*window, (j*window)+window)])
        # print(x)
        # print(y)
  plt.scatter(x, y,color='red')
  plt.title("window= %s  threshold= %s"%(window,threshold))
  plt.show()

dot_matrix(data1,data2,15,100)