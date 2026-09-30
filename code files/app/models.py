from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class TopicRequest(BaseModel):
    topic: str


class SummaryRequest(BaseModel):
    text: str


class SubjectRequest(BaseModel):
    subject: str