from collections import Counter

def MinWindowSubstring(strArr):
  """ array with 2 positions where 1st pos has a string with a lot of characters and second one,
        has the string you need to find in first string. Applying the Min Window subString algorithm, to get the smaller substring from first string, 
        that contains second string or at least contains all characters from second string.

  Args:
      strArr (_type_): array with 2 strings.

  Returns:
      _type_: retrieves the smallest substring.
  """  
  N,K = strArr
  word = N
  counterK = Counter(K)
  i = 0
  j = 1
  flag = True
  while flag:
    if j == len(N):
       flag = False
    subString = N[i:j+1] # current subString
    cont = 0 # counter to check if the substring contains all characters
    for k in counterK:
      if subString.count(k) >= counterK[k]:
        cont+=1
    if cont == len(counterK):
      if len(subString) < len(word):
        word = subString
        i+=1
      else:
        # this controls when the smallest substring if it is at the end of the array
        for b in range(0,len(subString)):
          shortW = subString[i+1:j+1] # same functionality as subString but different name
          cont2 = 0 # same functionality as cont but different name
          for k in counterK:
            if shortW.count(k) >= counterK[k]:
              cont2+=1
          if cont2 == len(counterK):
            if len(shortW) < len(word):
              word = shortW
              i+=1
        flag = False
    else:
      j+=1
  return word
# keep this function call here 
print(MinWindowSubstring(input()))