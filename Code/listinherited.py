class ListInherited:
    def __attrnames(self):
        result = ''
        for attr in dir(self):  # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':  # Skip internals
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,  # My class's name
            id(self),  # My address
            self.__attrnames())  # name=value list

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)