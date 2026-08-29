from celery import Celery

celery_app = Celery(
    "practice-api",
    broker="amqp://guest:guest@localhost:5672//",
    backend=None,
    include=[
        "services.practice_service004"
    ]
)

celery_app.conf.update(
    task_serializer = "json",
    result_serializer = "json",
    accept_content = ["json"],
    timezone = "UTC",
    enable_utc = True,
    control_queue_exclusive = True,
    event_queue_exclusive = True,
    worker_enable_remote_control = False,
    task_ignore_result = True
)