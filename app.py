from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

@app.get("/")
async def redirect() -> RedirectResponse:
    """Redirect to documentation endpoint.

    Returns:
        RedirectResponse: 
            The redirect HTTP response.
    """
    response = RedirectResponse(url='/docs')
    return response