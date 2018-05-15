import json

if __name__ == '__main__':
    consumer_key = 'qIhSaP3SDMjYTgQSHMnflOte0'
    consumer_secret = '7M4HGS8iPmma0tsC6KGMhqtlR4tDBl1YWPu1UtIMT5mvRNQw35'
    access_token = '3417237687-G6xlBPoHYQclCUhLoULgL6ubwiDjLmFUp1dEEqi'
    access_encrypted = 'zCDKTOHNFa31nBEGOhbttbA5RWX6lw7NR5jDsVJa3d6bh'
    data = {}
    data['ck'] = consumer_key
    data['cs'] = consumer_secret
    data['at'] = access_token
    data['ae'] = access_encrypted
    json_data = json.dumps(data)
    header = '[\n'
    ender = ']'
    obj = open('data/credentials.json', 'w')
    obj.write(header)
    obj.write(json_data + '\n')
    obj.write(ender)
    obj.close()
