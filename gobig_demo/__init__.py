from girder_worker import GirderWorkerPluginABC


class GobigDemoPlugin(GirderWorkerPluginABC):
    def task_imports(self):
        return ['gobig_demo.tasks']
