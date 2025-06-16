# BugPal

BugPal is a platform where developers post bugs or issues they encounter, and other developers provide solutions, patches, or collaborate to fix them. It includes a voting system for fixes, issue status management, user reputation, and notifications.

### Key Features:
* Issue Postings: Developers can post bugs, attach code snippets, and 
provide context (stack traces, steps to reproduce).

* Fix Proposals: Users can submit fixes (code, documentation, video).

* Voting: Users can upvote/downvote proposed solutions.

* Issue States: Track issues through various states (Open, In Progress, 
Solved, etc.).

* Notifications: Notify users when fixes are posted, and issues are updated.

* User Reputation: Reputation points based on contributions (posting fixes, 
upvotes).

* Admin Moderation: Admins can ban users or resolve flagged issues.


## State of Project

Part of the basic structure has been set-up. 
The following have been 
implemented (maybe not on all instances of the project yet):

* Project scaffolding using FastAPI and Poetry
* Async-ready SQLAlchemy 2.0 ORM setup
* PostgreSQL set-up with docker
* Database migrations via Alembic
* Layered architecture:
  * Models, DTOs, Repositories, Services, Routes
* Versioned Pydantic schemas for API stability
* Internal DTOs for decoupling services from schemas
* Implemented CRUD for:
  * Users
  * Issues
  * Fixes
* Applied design patterns:
  * Repository Pattern for database isolation
* Dependency injection for DB sessions
* Cleanly separated domain logic from transport and persistence layers
