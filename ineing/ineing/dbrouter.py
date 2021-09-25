class ProvidersRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'proveedores':
            return 'providers'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'proveedores':
            return 'providers'
        return None
