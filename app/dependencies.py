from fastapi import Request

from app.services.model_loader import ModelArtifact


def get_model_artifact(request: Request) -> ModelArtifact:
    return request.app.state.model_artifact