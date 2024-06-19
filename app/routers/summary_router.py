from fastapi import APIRouter
from langchain_huggingface import HuggingFacePipeline

from app.schemas.summary_schema import TextRequest

summary_router = APIRouter(
    tags=["summarize"],
)


@summary_router.post("/summarize")
async def summarize(request: TextRequest):
    summarizer = HuggingFacePipeline.from_model_id(model_id="facebook/bart-large-cnn",
                                                   task="summarization",
                                                   )

    summary = summarizer.invoke(request.text)
    return {"summary": summary}
