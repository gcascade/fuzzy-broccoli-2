class JobRegistry:
    _registry: dict[str, type] = {}

    @classmethod
    def register(cls, job_class: type) -> None:
        cls._registry[job_class.__name__] = job_class

    @classmethod
    def get_job_class(cls, job_type: str) -> type:
        job_class = cls._registry.get(job_type)
        if not job_class:
            raise ValueError(f"Unknown job type: {job_type}")
        return job_class
