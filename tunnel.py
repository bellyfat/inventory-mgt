
layers = ['|','¸','˛', '|', '.','◊', '.','=','/','∆','\\','~', '˘','†','¯','-','*','∏','ø','≈','<','<','','>','>']

colors = [
    '0;31;40m', # red
    '5;32;40m', # green flash
    '0;33;40m', # yellow    
    '5;34;40m', # blue flash
    '0;35;40m', # purple    
    '5;30;40m', # black flash
    '0;37;40m', # white
    '5;31;40m', # red flash
    '0;32;40m', # green
    '5;33;40m', # yellow flash  
    '0;34;40m', # blue
    '5;35;40m', # purple flash  
    '0;30;40m', # black flash
    '5;37;40m', # white flash
]

def set_color_scheme(text, color):
  return f'\x1b[{color}{text}\x1b[0m'

def tunnel(layers=[], size=None, offset=0):
  layers_length = len(layers)
  if size == None:
    size = layers_length
  if size % 2 == 0:
    size += 1
  if layers_length < 1:
    layers = list(range(8))

  for row in range(size//2):
    # if row < layers_length:
    x = row % layers_length
    # else:
    #   x = layers_length - (row - (layers_length - 1)) 
    
    for col in range(size//2):
      # if row+col>size-1:
      #   import pdb; pdb.set_trace()

      # this gives the top quadrant its shape
      

      # this gives the left quadrant its shape
      if row > col:
        layer_index = col % layers_length

      # elif row > row-col:
      #   layer_index = ( layers_length) - ( (row-1) % (layers_length ) ) - 1
      
      # this gives the right quadrant its shape
      elif row+col>size-1:
        layer_index = layers_length - (col - (layers_length - 1))
      else:
        layer_index = x


      
      try:   
        # this is where the indexing needs to change
        if col > size // 2:
          color = colors[layer_index%len(colors)]
          char = layers[ layer_index ]
        else:
          color = colors[ (layer_index%len(colors)) ]
          char = layers[layer_index]
      except IndexError:
        pass
        # print('index out of range', layer_index)

        
      # format color to char and space
      string = set_color_scheme(char, color)
      space = set_color_scheme(' ', color)

      # prints string without empty space instead of new line
      print(string, end=space)
    # print new line
    print('')


tunnel(layers, 40)
# tunnel(layers)
# tunnel(['0','-'])
# tunnel(['0','-'], 20)
