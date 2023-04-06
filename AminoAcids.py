

#dictionary of while loop values
codon = {"UUU" : " 🧬Phenylalanine🧬", "CUU" : " 🧬Leucine🧬", "AUU" : " 🧬Isoleucine🧬", "GUU" : " 🧬Valine🧬",
          "UUC" : " 🧬Phenylalanine🧬", "CUC" : " 🧬Leucine🧬", "AUC" : " 🧬Isoleucine🧬", "GUC" : " 🧬Valine🧬",
          "UUA" : " 🧬Leucine🧬", "CUA" : " 🧬Leucine🧬", "AUA" : " 🧬Isoleucine🧬", "GUA" : " 🧬Valine🧬",
          "UUG" : " 🧬Leucine🧬", "CUG" : " 🧬Leucine🧬", "AUG" : " 🧬Methionine🧬", "GUG" : " 🧬Valine🧬",
          "UCU" : " 🧬Serine🧬", "CCU" : " 🧬Proline🧬", "ACU" : " 🧬Threonine🧬", "GCU" : " 🧬Alanine🧬",
          "UCC" : " 🧬Serine🧬", "CCC" : " 🧬Proline🧬", "ACC" : " 🧬Threonine🧬", "GCC" : " 🧬Alanine🧬",
          "UCA" : " 🧬Serine🧬", "CCA" : " 🧬Proline🧬", "ACA" : " 🧬Threonine🧬", "GCA" : " 🧬Alanine🧬",
          "UCG" : " 🧬Serine🧬", "CCG" : " 🧬Proline🧬", "ACG" : " 🧬Threonine🧬", "GCG" : " 🧬Alanine🧬",
          "UAU" : " 🧬Isoleucine🧬", "CAU" : " 🧬Histidine🧬", "AAU" : " 🧬Asparagine🧬", "GAU" : " 🧬Aspartic Acid🧬",
          "UAC" : " 🧬Tyrosine🧬", "CAC" : " 🧬Histidine🧬", "AAC" : " 🧬Asparagine🧬", "GAC" : " 🧬Aspartic Acid🧬",
          "UAA" : " 🧬Stop Codon🧬", "CAA" : " 🧬Glutamine🧬", "AAA" : " 🧬Lysine🧬", "GAA" : " 🧬Glutamic Acid🧬",
          "UAG" : " 🧬Stop Codon🧬", "CAG" : " 🧬Glutamine🧬", "AAG" : " 🧬Lysine🧬", "GAG" : " 🧬Glutamic Acid🧬",
          "UGU" : " 🧬Cysteine🧬", "CGU" : " 🧬Arginine🧬", "AGU" : " 🧬Serine🧬", "GGU" : " 🧬Glycine🧬",
          "UGC" : " 🧬Cysteine🧬", "CGC" : " 🧬Arginine🧬", "AGC" : " 🧬Serine🧬", "GGC" : " 🧬Glycine🧬",
          "UGA" : " 🧬Stop Codon🧬", "CGA" : " 🧬Arginine🧬", "AGA" : " 🧬Arginine🧬", "GGA" : " 🧬Glycine🧬", "GGG" : " 🧬Glycine🧬"
          }

das = input('Please your 🧬DNA🧬 code in the letters A, G, C, T. Would you like to continue(Y/N)? ')
if das == 'Y':  


  loop1 = 0

  rna=""
  #replaces DNA with RNA letters
  while not loop1 == 1:
  #iterates over values
    loop1=0
    dna = input('What is your 🧬DNA🧬 code? ')
    dna = dna.upper()
    for i in range(0, len(dna)):
      if dna[i]=="T":
          rna=rna+"A"

      elif dna[i]=="G":
          rna=rna+"C"

      elif dna[i]=="A":
          rna=rna+"U"

      elif dna[i]=="C":
          rna=rna+"G"

      else:
        print("Error. Please ignore the following messages as they may be incorrect")
        loop1=2
        break
    if loop1==2:
      pass
    else:
      loop1=1

  print('Your 🧬DNA🧬 code is:', dna)
  print('The messenger 🧬RNA🧬 strand is: ', rna)
  a=0
  print("Your 🧬amino acid🧬 chain is:")
#divides string by 3, prints out corresponding amino acid
  for i in range(0, int(len(dna)/3)):
    print(codon[rna[a]+rna[a+1]+rna[a+2]])
    a=a+3
else: 
  print('Understood. Shutting down.')