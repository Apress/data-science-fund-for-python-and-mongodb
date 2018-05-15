if __name__ == "__main__":
    audio = {'amp':'Linn', 'preamp':'Luxman', 'speakers':'Energy',
             'ic':'Crystal Ultra', 'pc':'JPS', 'power':'Equi-Tech',
             'sp':'Crystal Ultra', 'cdp':'Nagra', 'up':'Esoteric'}
    del audio['up']
    print ('dict "deleted" element;')
    print (audio, '\n')
    print ('dict "added" element;')
    audio['up'] = 'Oppo'
    print (audio, '\n')
    print ('universal player:', audio['up'], '\n')
    dict_ls = [audio]
    video = {'tv':'LG 65C7 OLED', 'stp':'DISH', 'HDMI':'DH Labs',
             'cable' : 'coax'}
    print ('list of dict elements;')
    dict_ls.append(video)
    for i, row in enumerate(dict_ls):
        print ('row', i, ':')
        print (row)
