from .local_business import LocalBusiness


class FoodEstablishment(LocalBusiness):
    def __init__(self, object):
        LocalBusiness.__init__(self, object)
        self.type = "FoodEstablishment"
        self.servesCuisine = object['servesCuisine']
        self.acceptsReservations = object['acceptsReservations']

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
        if 'acceptsReservations' in object.keys():
            self.acceptsReservations = object['acceptsReservations']
        if 'servesCuisine' in object.keys():
            self.servesCuisine = object['servesCuisine']

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
        string += '<p> ' + 'ServesCuisine: {} </p>'.format(self.servesCuisine)
        string += '<p> ' + 'AcceptsReservations: {} </p>'.format(self.acceptsReservations)
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
        string += '\t- ' + 'ServesCuisine: {} \n'.format(self.servesCuisine)
        string += '\t- ' + 'AcceptsReservations: {} \n'.format(self.acceptsReservations)
        string += '\n'
        return string

    def to_xml(self):
        string = '<FoodEstablishment>'
        string += '<Id> {} </Id>'.format(self.id)
        string += '<@Type> {} </@Type>'.format(self.type)
        string += '<@Context> {} </@Context>'.format(self.context)
        string += '<Name> {} </Name>'.format(self.name)
        string += '<Address> {} </Address>'.format(self.address)
        string += '<Description> {} </Description>'.format(self.description)
        string += '<Telephone> {} </Telephone>'.format(self.telephone)
        string += '<Url> {} </Url>'.format(self.url)
        string += '<OpeningHours> {} </OpeningHours>'.format(self.openingHours)
        string += '<ServesCuisine> {} </ServesCuisine>'.format(self.servesCuisine)
        string += '<AcceptsReservations> {} </AcceptsReservations>'.format(self.acceptsReservations)
        string += '</FoodEstablishment>'
        return string

