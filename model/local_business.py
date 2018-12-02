import json


class LocalBusiness:
    def __init__(self, object):
        self.context = "http://schema.org"
        self.type = "LocalBusiness"
        self.address = object['address']
        self.description = object['description']
        self.name = object['name']
        self.telephone = object['telephone']
        self.url = object['url']
        self.openingHours = object['openingHours']

    def actualizar(self, object):
        if 'address' in object.keys():
            self.address = object['address']
        if 'description' in object.keys():
            self.description = object['description']
        if 'name' in object.keys():
            self.name = object['name']
        if 'telephone' in object.keys():
            self.telephone = object['telephone']
        if 'url' in object.keys():
            self.url = object['url']
        if 'openingHours' in object.keys():
            self.openingHours = object['openingHours']

    def to_html(self):
        string = '<section> <h3> Tipo {} </h3>'.format(self.type)
        string += '<p> ' + 'Id: {} </p>'.format(self.id)
        string += '<p> ' + '@Type: {} </p>'.format(self.type)
        string += '<p> ' + '@Context: {} </p>'.format(self.context)
        string += '<p> ' + 'Name: {} </p>'.format(self.name)
        string += '<p> ' + 'Adress: {} </p>'.format(self.address)
        string += '<p> ' + 'Description: {} </p>'.format(self.description)
        string += '<p> ' + 'Telephone: {} </p>'.format(self.telephone)
        string += '<p> ' + 'Url: {} </p>'.format(self.url)
        string += '<p> ' + 'OpeningHours: {} </p>'.format(self.openingHours)
        string += '</section>'
        return string

    def to_text(self):
        string = 'Tipo: {} \n'.format(self.type)
        string += '\t- ' + 'Id: {} \n'.format(self.id)
        string += '\t- ' + '@Type: {} \n'.format(self.type)
        string += '\t- ' + '@Context: {} \n'.format(self.context)
        string += '\t- ' + 'Name: {} \n'.format(self.name)
        string += '\t- ' + 'Adress: {} \n'.format(self.address)
        string += '\t- ' + 'Description: {} \n'.format(self.description)
        string += '\t- ' + 'Telephone: {} \n'.format(self.telephone)
        string += '\t- ' + 'Url: {} \n'.format(self.url)
        string += '\t- ' + 'OpeningHours: {} \n'.format(self.openingHours)
        string += '\n'
        return string

    def to_xml(self):
        string = '<LocalBusiness>'
        string += '<Id> {} </Id>'.format(self.id)
        string += '<@Type> {} </@Type>'.format(self.type)
        string += '<@Context> {} </@Context>'.format(self.context)
        string += '<Name> {} </Name>'.format(self.name)
        string += '<Address> {} </Address>'.format(self.address)
        string += '<Description> {} </Description>'.format(self.description)
        string += '<Telephone> {} </Telephone>'.format(self.telephone)
        string += '<Url> {} </Url>'.format(self.url)
        string += '<OpeningHours> {} </OpeningHours>'.format(self.openingHours)
        string += '</LocalBusiness>'
        return string

    def to_json(self):
        string = json.dumps( self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        string = string.replace('type', '@type')
        string = string.replace("context", "@context")
        return string
