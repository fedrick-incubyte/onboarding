"""Unit tests for the Project ORM model."""


def should_have_user_id_on_project():
    from app.models.project import Project
    assert hasattr(Project, "user_id")


def should_have_user_relationship_on_project():
    from app.models.project import Project
    assert hasattr(Project, "user")
