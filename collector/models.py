# models.py
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class UploadRequest(BaseModel):
    """User-provided context accompanying an upload."""
    source: Optional[str] = Field(default=None, description="Where the sample comes from.")
    tags: Optional[List[str]] = Field(default=None, description="Optional labels.")
    note: Optional[str] = Field(default=None, description="Optional notes.")


class PEMetadata(BaseModel):
    """Selected PE metadata via pefile (Windows Portable Executable)."""
    pe_type: Optional[str] = None
    imphash: Optional[str] = None
    timestamp_unix: Optional[int] = None
    timestamp_iso: Optional[str] = None
    machine: Optional[str] = None
    number_of_sections: Optional[int] = None
    characteristics: Optional[str] = None
    sections: Optional[List[Dict[str, Any]]] = None
    imports: Optional[Dict[str, List[str]]] = None


class ELFBasicMetadata(BaseModel):
    """Selected ELF metadata via LIEF (Linux)."""
    class_type: Optional[str] = None
    machine: Optional[str] = None
    entrypoint: Optional[int] = None
    libraries: Optional[List[str]] = None


class MachOBasicMetadata(BaseModel):
    """Selected Mach-O metadata via LIEF (macOS)."""
    filetype: Optional[str] = None
    cpu_type: Optional[str] = None
    entrypoint: Optional[int] = None
    libraries: Optional[List[str]] = None


class FileMetadata(BaseModel):
    """Unified metadata model saved alongside the sample."""
    filename: str
    size_bytes: int
    md5: str
    sha1: str
    sha256: str
    ssdeep: Optional[str] = None
    mime_magic: Optional[str] = None
    ext: Optional[str] = None
    entropy: Optional[float] = None
    file_kind: Optional[str] = None
    pe: Optional[PEMetadata] = None
    elf: Optional[ELFBasicMetadata] = None
    macho: Optional[MachOBasicMetadata] = None
    external_providers: Dict[str, Dict[str, Any]] = Field(default_factory=dict,)


class UploadResponse(BaseModel):
    """API response after storing a sample + metadata JSON."""
    id: str  # use sha256 as ID
    stored_path: str
    metadata_path: str
    metadata: FileMetadata
    received_at: datetime
    source: Optional[str] = None
    tags: Optional[List[str]] = None
    note: Optional[str] = None

# models.py (aggiunte)
from typing import List, Dict, Any
from pydantic import BaseModel

class MetadataSearchResponse(BaseModel):
    """List of stored metadata objects that matched the query."""
    count: int
    results: List[Dict[str, Any]]
