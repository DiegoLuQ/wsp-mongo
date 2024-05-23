from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

class Model_Usuario(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id", validate_default=True)
    wsp_text: Optional[str] = None
    wsp_name: Optional[str] = None
    # fecha : datetime = Field(default_factory=datetime.today)
    wsp_number: Optional[str] = None
    wsp_wamid: Optional[str] = None
    wsp_timestamp: Optional[str] = None
    wsp_display_phone_number: Optional[str] = None
    
    model_config: ConfigDict = ConfigDict(arbitrary_types_allowed=True, json_schema_extra={
        "example":   {
            "wsp_text":"personal_cod:pw1",
            "wsp_name":"JD",
            "wsp_number" : "56961227637",
            "wsp_wamid": "wamid.HBgLNTY5NjEyMjc2MzcVAgASGBYzRUIwRTc5MkQ4RkNBODZGMjdGNkFGAA=",
            "wsp_timestamp": "1713987026",
            "wsp_display_phone_number":"56934888609"
        }})
                                          