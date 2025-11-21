"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Company-specific schemas

class Inquiry(BaseModel):
    """
    Customer inquiries submitted from the website contact form.
    Collection name: "inquiry"
    """
    name: str = Field(..., description="Full name of the person reaching out")
    email: EmailStr = Field(..., description="Contact email address")
    phone: Optional[str] = Field(None, description="Phone number")
    subject: Optional[str] = Field(None, description="Subject or reason for contact")
    message: str = Field(..., description="Message or project details")

class Service(BaseModel):
    """
    Services your electrical company offers.
    This can be used if you decide to manage services via the database later.
    Collection name: "service"
    """
    title: str = Field(..., description="Service title, e.g., 'Residential Wiring'")
    description: Optional[str] = Field(None, description="Short description of the service")
    icon: Optional[str] = Field(None, description="Icon name for UI use")
    featured: bool = Field(False, description="Whether this service is featured on the homepage")
