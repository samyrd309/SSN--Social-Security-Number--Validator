class SSN(object):
  def ssnValidator(ssnInput):
    blocks = ssnInput.split('-')
    if len(blocks) == 3 and ssnInput != '':
      first = blocks[0]
      second = blocks[1]
      third = blocks[2]
      if len(first) == 3 and len(second) == 2 and len(third) == 4:
        if (first == '000' or first== '666') or (int(first) >= 900 and int(first) <=999):
          ssnOutput = 'Invalid code. The first part should not be 000, 666, or between 900 and 999'
          print(ssnOutput)
          return ssnOutput
        elif int(second)< 1 or int(second) > 99:
          ssnOutput = 'Invalid code. The second part should be from 01 to 99'
          print(ssnOutput)
          return ssnOutput
        elif int(third) < 1 or int(third) > 9999:
          ssnOutput = 'Invalid code. The third part should be from 0001 to 9999'
          print(ssnOutput)
          return ssnOutput
        else:
          ssnOutput = 'valid SSN code'
          print(ssnOutput)
        return ssnOutput
      else:
        ssnOutput = 'Invalid length input'
        print(ssnOutput)
        return ssnOutput 
    else:
      ssnOutput = 'Invalid length input'
      print(ssnOutput)
      return ssnOutput
  ssnInput = input('Insert your code SSN: ')
  ssnValidator(ssnInput)