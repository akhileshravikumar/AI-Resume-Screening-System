from fastapi import FastAPI
from pydantic import BaseModel
from app.model import dummy_predict

app = FastAPI()

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/score_resume")
def score_resume(data: ResumeRequest):
    score = dummy_predict(data.resume_text, data.job_description)
    return {"match_score": round(score * 100, 2)}
