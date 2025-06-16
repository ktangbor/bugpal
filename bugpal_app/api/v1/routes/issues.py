from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from bugpal_app.api.v1.schemas.issue import IssueCreate, IssueRead
from bugpal_app.services.issue import IssueService
from bugpal_app.depedencies import get_db

router = APIRouter(prefix="/issues", tags=["Issues"])

@router.post("/", response_model=IssueRead)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    service = IssueService(db)
    return service.create_issue(issue)

@router.get("/", response_model=list[IssueRead])
def list_issues(db: Session = Depends(get_db)):
    service = IssueService(db)
    return service.list_issues()

@router.get("/{issue_id}", response_model=IssueRead)
def get_issue(issue_id: int, db: Session = Depends(get_db)):
    service = IssueService(db)
    issue = service.get_issue(issue_id)
    if not issue:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue
