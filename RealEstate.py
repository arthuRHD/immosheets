class RealEstate: # RealEstate item
    """Definition of a real estate item, it can be a flat or a house."""

    def __init__(self, id_announce, title, description, surface, price, latitude, longitude): # RealEstate constructor
        """Build of RealEstate object from its attributes"""
        self.id_announce = id_announce
        self.title = title
        self.description = description
        self.surface = surface
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        """Representation of the object"""
        return "RealEstate: title({}), description({}), surface({}), prix({})".format(
                    self.title, self.description, self.surface, self.price
                )

    def __str__(self):
        """String representation of the object"""
        return "title({}), description({}), surface({}), prix({})".format(
                self.title, self.description, self.surface, self.price)

    def to_csv(self):
        """Transform the object in a standard CSV format"""
        csv = "\"{}\", \"{}\", \"{}\", \"{}\"".format(
            self.title, self.description, self.surface, self.price
        )
        return csv