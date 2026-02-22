"""
Application configuration and settings
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # LLM Provider — choose one: openai, gemini, claude
    llm_provider: str = "gemini"
    llm_model: str = "gemini-2.0-flash"
    llm_temperature: float = 0.0

    # Embedding Provider — choose one: openai, gemini
    embedding_provider: str = "gemini"
    embedding_model: str = "models/text-embedding-004"

    # API Keys — provide only the key(s) for your chosen provider(s)
    openai_api_key: Optional[str] = None
    google_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_workers: int = 4
    
    # ChromaDB Configuration
    chromadb_path: str = "./knowledge_base"
    chromadb_collection: str = "knowledge_base"
    
    # RAG Configuration
    rag_top_k: int = 3
    rag_score_threshold: float = 0.2
    
    # Application Settings
    max_query_length: int = 500
    rate_limit_per_minute: int = 10
    session_timeout_hours: int = 24
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "agent.log"
    
    # Security
    allowed_origins: str = "http://localhost:8000,http://localhost:3000"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()


# Helper function to get settings
def get_settings() -> Settings:
    """Get application settings"""
    return settings


def get_llm():
    """Return an LLM instance based on the llm_provider setting."""
    provider = settings.llm_provider.lower()
    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            openai_api_key=settings.openai_api_key
        )
    elif provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            google_api_key=settings.google_api_key
        )
    elif provider == "claude":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model=settings.llm_model,
            temperature=settings.llm_temperature,
            anthropic_api_key=settings.anthropic_api_key
        )
    else:
        raise ValueError(
            f"Unsupported LLM provider: '{provider}'. "
            "Valid options: openai, gemini, claude"
        )


def get_embeddings():
    """Return an embeddings instance based on the embedding_provider setting."""
    provider = settings.embedding_provider.lower()
    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key
        )
    elif provider == "gemini":
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        return GoogleGenerativeAIEmbeddings(
            model=settings.embedding_model,
            google_api_key=settings.google_api_key
        )
    else:
        raise ValueError(
            f"Unsupported embedding provider: '{provider}'. "
            "Valid options: openai, gemini"
        )
