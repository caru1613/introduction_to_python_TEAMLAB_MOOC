import configparser

config = configparser.ConfigParser()
config.sections() #no section as file is not choosen.

config.read('example.cfg')
config.sections()


for key in config['SectionOne']:
    print(key)

config['SectionOne']['Status']
