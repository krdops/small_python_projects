machine_list = [{
    'name':'Saturn',
    'number': 8,
    'waste': [],
    'weight': 0,
    'msfproduced':0,
    'percentwaste': 0
},{'name':'1224',
     'number':9,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'Bobst',
     'number': 12,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'1636',
     'number': 35,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'EMBA',
     'number': 38,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'618',
     'number': 40,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'1622',
     'number': 41,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'Expertfold',
     'number': 42,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'5 Color',
     'number': 45,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'1228A',
     'number': 46,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'1228B',
     'number': 47,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'924',
     'number': 48,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'Mckinley',
     'number': 90,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
},{'name':'1628',
     'number': 120,
     'waste':[],
     'weight': 0,
     'msfproduced':0,
     'percentwaste': 0
}]



class wasteClass():


  def enter_waste():
      while True:
          machine_selection = str(input('Please enter which machine you would like to enter the waste for: '))
          for element in machine_list:
              if machine_selection == element['name']:
                  print('You Have Selected: {}'.format(element['name']))
                  waste_input = int(input('Please enter the waste for this period: '))
                  element['waste'].append(waste_input)
                  if str(input('Do you want to continue? yes/no: ')) == 'no':
                      print("\nHere's everything as entered: \n")
                      for i, machine in enumerate(machine_list):
                          print(i, machine)
                      return False

  def enter_weight():
      while True:    
          machine_selection = str(input('Please enter which machine you would like to enter the produced weight for: '))
          for element in machine_list:
              if machine_selection == element['name']:
                  print('You have selected: {}'.format(element['name']))
                  weight_input = int(input('Please enter weight produced for this period: '))
                  element['weight'] = weight_input
                  if str(input('Do you want to continue? yes/no: ')) == 'no':
                      print("\nHere's everything as entered: \n")
                      for i, machine in enumerate(machine_list):
                          print(i, machine)
                      return False
                  
                      

  def enter_msf():
      machine_selection = str('Please enter which machine you would like to enter the MSF for: ')
      for element in machine_list:
          if machine_selection == element['name']:
              print('You have selected: {}'.format(element['name']))
              msf_input = int(input('Please enter MSF produced for this period: '))
              element['msfproduced'] = msf_input
              if str(input('Do you want to continue? yes/no: ')) == 'no':
                  print("\nHere's everything as entered: \n")
                  for i, machine in enumerate(machine_list):
                      print(i, machine)
                      return False

  def total_waste():
      for i, machine in enumerate(machine_list):
          print('')
          total = sum(machine['waste'])
          print(i, "Machine: {}\nWaste Total: {:,}\n".format(machine['name'], total))
          return total

  def calculate_waste_percentage():

    try:
      for element in machine_list:
       
          if sum(element['waste'])/element['weight'] != 0:
              percentage = (sum(element['waste'])/element['weight']) * 100
          else:
              continue
          element['percentwaste'] = percentage
          print('Machine: {}\nWeight Produced: {:,}\n% of Waste: {}%'.format(element['name'], element['weight'], percentage ))
    except ZeroDivisonError:
        print("Divison by Zero Error")
          



  def save_to_file():
      filename = str(input('Please name your file, with no spaces or special characters: '))
      with open('{}.txt'.format(filename), 'w') as f:
          f.write('Machine Waste Report\n\n')
          for machine in machine_list:
              f.write(machine['name'] + '\n')
              f.write('Total Waste: ' + str(sum(machine['waste'])))
              f.write('\n\n')    
   
    

if __name__ == '__main__':
  

  wasteClass.enter_waste()
  wasteClass.enter_weight()
  wasteClass.enter_msf()
  wasteClass.calculate_waste_percentage()
