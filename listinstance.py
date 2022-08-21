class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                    self.__class__.__name__, # My class's name
                    id(self), # My address
                    self.__attrnames()) # name=value list
if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)