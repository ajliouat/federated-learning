import syft as sy

def secure_aggregation(models):
    hook = sy.TorchHook(torch)
    workers = [sy.VirtualWorker(hook, id=f"client_{i}") for i in range(len(models))]
    for i, model in enumerate(models):
        model.send(workers[i])
    aggregated_model = models[0].copy()
    for model in models[1:]:
        aggregated_model += model
    aggregated_model.get()
    return aggregated_model