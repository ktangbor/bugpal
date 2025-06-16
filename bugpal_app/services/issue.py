from sqlalchemy.orm import Session
from bugpal_app.repos.issue import IssueRepository
from bugpal_app.api.v1.schemas.issue import IssueCreate
from bugpal_app.models.issue import Issue

class IssueService:
    def __init__(self, db: Session):
        self.repo = IssueRepository(db)

    def create_issue(self, issue: IssueCreate) -> Issue:
        return self.repo.create(issue)

    def get_issue(self, issue_id: int) -> Issue|None:
        return self.repo.get(issue_id)

    def list_issues(self) -> list[Issue]:
        return self.repo.list()
