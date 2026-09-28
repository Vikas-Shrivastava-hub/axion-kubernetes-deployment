"""
Axion Telemetry Query Service - Configuration
"""

import os
from dataclasses import dataclass

@dataclass
class Settings:
    # PostgreSQL connection string
    # Format: postgresql://<user>:<password>@<host>:<port>/<database>
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://axion:Vikasshrivastava%4023081998@axion1server.postgres.database.azure.com:5432/axion_db",
    )
    # Allows configuring a different port, e.g., if we run multiple services
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
