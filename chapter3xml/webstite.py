class Dispatcher:
    def dispatcher(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default' + prefix.capitalize();
        method = getattr(self, mname, None)
        if callable(method):
            args = ()
        else:
            method = getattr(self, dname, None)
            args = name
        if prefix == 'start': args += attrs,
