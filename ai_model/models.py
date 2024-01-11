from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def execute_plugin_method(self, plugin_name, method_name, *args, **kwargs):
        try:
            plugin = self.plugins.get(name=plugin_name)
            method = getattr(plugin, method_name)
            return method(*args, **kwargs)
        except Exception as e:
            if 'not logged in' in str(e):
                self.execute_plugin_method(plugin_name, 'login')
                return self.execute_plugin_method(plugin_name, method_name, *args, **kwargs)
            else:
                raise e

    class Meta:
        verbose_name = "AI Model"
        verbose_name_plural = "AI Models"