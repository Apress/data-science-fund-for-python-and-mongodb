import pandas as pd

if __name__ == "__main__":
    df = pd.read_json("data/audio.json")    
    amps = df[df.desc == 'amplifier']
    print (amps, '\n')
    price = df.query('price >= 40000')
    print (price, '\n')
    between = df.query('4999 < price < 6000')
    print (between, '\n')
    row = df.loc[[0, 10, 19]]
    print (row)
