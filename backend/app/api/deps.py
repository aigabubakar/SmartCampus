from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.session import get_db
from app.models.user import User
from app.core.security import decode_access_token

# HTTP Bearer token extractor (auto_error=False allows custom error handling)
security_scheme = HTTPBearer(auto_error=False)

def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Validate incoming JWT Bearer token and retrieve authenticated User from database.
    Raises 401 Unauthorized if token is missing, invalid, expired, or user not found.
    Raises 403 Forbidden if user account is deactivated/suspended.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required. Please provide a valid Bearer token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = credentials.credentials
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired or invalid token signature. Please re-authenticate.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Malformed token claims.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authenticated user account no longer exists in database.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Institutional account is suspended. Please contact the Academic Registrar.",
        )

    return user

def get_optional_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security_scheme),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """Retrieve current user if valid bearer token is supplied; otherwise None."""
    if not credentials or not credentials.credentials:
        return None
    try:
        return get_current_user(credentials=credentials, db=db)
    except HTTPException:
        return None

def require_roles(allowed_roles: List[str]):
    """
    Factory dependency to enforce Role-Based Access Control (RBAC).
    Root super-administrators (is_root=True) bypass role restrictions.
    """
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.is_root:
            return current_user

        normalized_user_role = current_user.role.lower().strip()
        normalized_allowed = [r.lower().strip() for r in allowed_roles]

        # Alias lecturer/teacher
        if normalized_user_role == "teacher":
            normalized_user_role = "lecturer"

        if normalized_user_role not in normalized_allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Security Clearance Denied: Role '{current_user.role}' lacks authorization for this operation."
            )
        return current_user

    return role_checker
