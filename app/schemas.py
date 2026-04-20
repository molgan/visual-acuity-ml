from pydantic import BaseModel, Field, ConfigDict
from typing import Literal


class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    age: int | None = Field(default=None, ge=0, le=120, description="Patient age (years)")
    sex: Literal[0, 1] | None = Field(default=None, description="Sex (0 = female, 1 = male)")
    manifest_sphere: float | None = Field(default=None, ge=-30, le=30, description="Manifest (non-cycloplegic) spherical refraction (D)")
    cyclo_sphere: float | None = Field(default=None, ge=-30, le=30, description="Cycloplegic spherical refraction (D)")
    cyclo_cylinder: float | None = Field(default=None, ge=-15, le=15, description="Cycloplegic cylindrical refraction (D)")
    keratometry_cylinder: float | None = Field(default=None, ge=-15, le=15, description="Keratometric cylinder (D)")
    k1_flat: float | None = Field(default=None, ge=30, le=70, description="K1 (flat meridian keratometry) (D)")
    axial_length: float | None = Field(default=None, ge=14, le=40, description="Axial length (mm)")
    pupil_diameter: float | None = Field(default=None, ge=0, le=12, description="Pupil diameter (mm)")


class PredictionResponse(BaseModel):
    prediction: float
    model_name: str
    model_version: str
    imputed_fields: list[str]
    warnings: list[str] = Field(default_factory=list)


class BatchPredictionRequest(BaseModel):
    items: list[PredictionRequest] = Field(
        ...,
        min_length=1,
        description="List of input records for batch prediction",
    )


class BatchPredictionItemResponse(BaseModel):
    prediction: float
    imputed_fields: list[str]
    warnings: list[str] = Field(default_factory=list)


class BatchPredictionResponse(BaseModel):
    model_name: str
    model_version: str
    predictions: list[BatchPredictionItemResponse]