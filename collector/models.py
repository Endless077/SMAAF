#     ____    ____               __        __          
#    |_   \  /   _|             |  ]      [  |         
#      |   \/   |   .--.    .--.| | .---.  | |  .--.   
#      | |\  /| | / .'`\ \/ /'`\' |/ /__\\ | | ( (`\]  
#     _| |_\/_| |_| \__. || \__/  || \__., | |  `'.'.  
#    |_____||_____|'.__.'  '.__.;__]'.__.'[___][\__) ) 
#                                                      

# Imports
from typing import List, Dict, Literal, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime

###################################################################################################

# ================= ELF/MachO/PE =================
class ELFBasicMetadata(BaseModel):
    class_type: Optional[str] = None
    machine: Optional[str] = None
    entrypoint: Optional[int] = None
    libraries: Optional[List[str]] = None

class MachOBasicMetadata(BaseModel):
    filetype: Optional[str] = None
    cpu_type: Optional[str] = None
    entrypoint: Optional[int] = None
    libraries: Optional[List[str]] = None

class PEMetadata(BaseModel):
    pe_type: Optional[str] = None
    imphash: Optional[str] = None
    timestamp_unix: Optional[int] = None
    timestamp_iso: Optional[str] = None
    machine: Optional[str] = None
    number_of_sections: Optional[int] = None
    characteristics: Optional[str] = None
    sections: Optional[List[Dict[str, Any]]] = None
    imports: Optional[Dict[str, List[str]]] = None

###################################################################################################

# ================= Metadata =================
class FileMetadata(BaseModel):
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

###################################################################################################

# ================= Requests =================
class UploadRequest(BaseModel):
    tags: Optional[List[str]] = Field(default=None)
    source: Optional[str] = Field(default=None)
    note: Optional[str] = Field(default=None)

class SearchRequest(BaseModel):
    query: Optional[str] = None
    tags: Optional[List[str]] = None
    tags_mode: Literal["any", "all"] = "any"
    source: Optional[str] = None
    ext: Optional[str] = None
    file_kind: Optional[str] = None
    mime_contains: Optional[str] = None
    min_size: Optional[int] = Field(None, ge=0)
    max_size: Optional[int] = Field(None, ge=0)
    since: Optional[str] = None
    until: Optional[str] = None

class UpdateRequest(BaseModel):
    sample: str
    provider: Literal["virustotal", "virusshare", "malwarebazaar"]

# ================= Responses =================
class UploadResponse(BaseModel):
    id: str
    stored_path: str
    metadata_path: str
    metadata: FileMetadata
    tags: Optional[List[str]] = None
    source: Optional[str] = None
    note: Optional[str] = None
    upload_time: datetime

class UpdateResponse(BaseModel):
    status: str
    sample: str
    provider: str
    update: dict

class SearchResponse(BaseModel):
    count: int
    results: List[Dict[str, Any]]

###################################################################################################
