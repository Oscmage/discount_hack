from starlette.responses import JSONResponse

NO_CODE_AVAILABLE_ERROR = JSONResponse(
    status_code=404, content={"message": "No code available"}
)
