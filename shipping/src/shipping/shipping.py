class ShippingContainer:

    # Class attribute
    next_serial = 1337

    # Use static methods when there is no access to either class or instance objects
    # Most likely an implementation detail of the class
    # May be able to be moved outside the class to become a global-scope function in the module
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result 
    
    # Use class methods when it requires access to the class object to call other class methds or the constructor
    @classmethod
    def _generate_serial_cls(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Factory method which returns an isntance of a class.
    # The method name allows callers to express intent, and allows construction to be performed with different combinations of arguments
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        # Instance attributes
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial_cls()